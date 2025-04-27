# src/app/webapp.py

import streamlit as st
import json
import re

# Importaciones necesarias
from src.core.generator import generate_exercise
from src.core.solver import solve_exercise
from config.dataset_config import TEMAS_SUBTEMAS, PERFILES, DIFICULTADES, TIPOS_ACTIVIDAD

# === Funciones utilitarias ===

def extraer_nombres(opciones_con_descripcion):
    """Extrae el nombre principal de una lista de opciones con descripciones."""
    return {op.split(":")[0]: op for op in opciones_con_descripcion}

def extraer_temas_subtemas_con_nombres(temas_subtemas):
    """Separa temas y subtemas en dos mapas accesibles."""
    temas_map = {k.split(":")[0]: k for k in temas_subtemas}
    subtemas_map = {}
    for tema_key, subtemas in temas_subtemas.items():
        subtemas_map[tema_key.split(":")[0]] = {s.split(":")[0]: s for s in subtemas}
    return temas_map, subtemas_map


def convertir_latex_a_markdown(texto):
    """Convierte comandos simples de LaTeX a Markdown y corrige saltos de línea."""
    # Negrita
    texto = re.sub(r'\\textbf\{(.*?)\}', r'**\1**', texto)
    # Cursiva
    texto = re.sub(r'\\textit\{(.*?)\}', r'*\1*', texto)
    # Corregir saltos de línea
    texto = texto.replace("\\n", "\n\n")  # Streamlit necesita doble salto o se puede usar <br> también
    return texto

def render_solution(solution):
    """Renderiza texto normal y fórmulas LaTeX en Streamlit, corrigiendo formato."""
    # Dividir en bloques de texto y fórmulas
    blocks = re.split(r"(\$\$.*?\$\$|\$.*?\$)", solution, flags=re.DOTALL)

    for block in blocks:
        block = block.strip()
        if not block:
            continue
        if block.startswith('$$') and block.endswith('$$'):
            st.latex(block[2:-2].strip())  # Fórmulas grandes
        elif block.startswith('$') and block.endswith('$'):
            st.latex(block[1:-1].strip())  # Fórmulas inline
        else:
            texto_convertido = convertir_latex_a_markdown(block)
            st.markdown(texto_convertido)



def main():
    # Configuración de la página
    st.set_page_config(page_title="Generador de Ejercicios 4º ESO", layout="centered")
    st.title("Generador Inteligente de Ejercicios de Matemáticas")
    st.markdown("¡Crea ejercicios personalizados para tus alumnos en segundos! ✨")
    st.markdown("---")

    # Preprocesamiento de las opciones
    perfiles_map = extraer_nombres(PERFILES)
    dificultades_map = extraer_nombres(DIFICULTADES)
    tipos_map = extraer_nombres(TIPOS_ACTIVIDAD)
    temas_map, subtemas_map = extraer_temas_subtemas_con_nombres(TEMAS_SUBTEMAS)

    with st.expander("📚 Selección del ejercicio", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            tema_nombre = st.selectbox("🧭 Tema principal", list(temas_map.keys()))
            tema = temas_map[tema_nombre]
        with col2:
            subtema_nombre = st.selectbox("🔍 Subtema específico", list(subtemas_map[tema_nombre].keys()))
            subtema = subtemas_map[tema_nombre][subtema_nombre]

        col3, col4 = st.columns(2)
        with col3:
            dificultad_nombre = st.selectbox("📈 Nivel de dificultad", list(dificultades_map.keys()))
            dificultad = dificultades_map[dificultad_nombre]
        with col4:
            tipo_nombre = st.selectbox("✏️ Tipo de actividad", list(tipos_map.keys()))
            tipo = tipos_map[tipo_nombre]

        perfil_nombre = st.selectbox("👤 Perfil del alumno", list(perfiles_map.keys()))
        perfil = perfiles_map[perfil_nombre]

        detalles_adicionales = st.text_area("📝 Detalles adicionales (opcional)", height=100)

    st.markdown("---")

    # Generar Ejercicio
    if st.button("🚀 Generar Ejercicio", use_container_width=True):
        with st.spinner("Generando ejercicio..."):
            # Llamar a la función del core para generar el enunciado del ejercicio
            enunciado = generate_exercise(tema, subtema, dificultad, tipo, perfil, detalles_adicionales)
            print("Enunciado generado:", enunciado)

        # Transformar respuesta JSON
        try:
            enunciado = enunciado.replace("'", '"').replace("```json", "").replace("```", "")
            response_json = json.loads(enunciado)
            st.session_state["ultimo_enunciado"] = response_json.get("enunciado", "Error: 'enunciado' no encontrado en la respuesta.")
        except json.JSONDecodeError:
            st.error("Error al procesar la respuesta del modelo. Asegúrate de que sea un JSON válido.")
            st.session_state["ultimo_enunciado"] = "Error: No se pudo generar el enunciado."

        # Guardar sesión
        st.session_state["ultimo_tema"] = tema
        st.session_state["ultimo_subtema"] = subtema
        st.session_state["ultimo_perfil"] = perfil
        st.session_state["mostrar_solucion"] = False

    # Mostrar enunciado y botón de resolución
    if "ultimo_enunciado" in st.session_state:
        st.subheader("📄 Enunciado")
        render_solution(st.session_state["ultimo_enunciado"])
        # st.markdown(st.session_state["ultimo_enunciado"], unsafe_allow_html=True)

        if st.button("🧠 Ver Resolución Paso a Paso", use_container_width=True):
            st.session_state["mostrar_solucion"] = True

        if st.session_state.get("mostrar_solucion"):
            with st.spinner("Generando resolución paso a paso..."):
                # Llamar a la función del core para generar la solución
                solucion = solve_exercise(st.session_state["ultimo_tema"], st.session_state["ultimo_subtema"], st.session_state["ultimo_enunciado"], st.session_state["ultimo_perfil"])

            try:
                solucion = solucion.replace("'", '"').replace("```json", "").replace("```", "")
                response_json = json.loads(solucion)
                st.session_state["ultima_solucion"] = response_json.get("solucion", "Error: 'sol' no encontrado en la respuesta.")
            except json.JSONDecodeError:
                st.error("Error al procesar la respuesta del modelo. Asegúrate de que sea un JSON válido.")
                st.session_state["ultima_solucion"] = "Error: No se pudo generar la solución."

            render_solution(st.session_state["ultima_solucion"])

    st.markdown("---")
    st.caption("Desarrollado para prácticas del Máster en Formación del Profesorado · 2025")


if __name__ == "__main__":
    main()
