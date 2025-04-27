import streamlit as st
from config.prompts_config import TEMAS_SUBTEMAS, PERFILES, DIFICULTADES, TIPOS_ACTIVIDAD
from code.generator import generate_exercise, generate_image
from code.solver import solve_exercise
import json
import re

# === Función utilitaria ===
def extraer_nombres(opciones_con_descripcion):
    return {op.split(":")[0]: op for op in opciones_con_descripcion}

def extraer_temas_subtemas_con_nombres(temas_subtemas):
    temas_map = {k.split(":")[0]: k for k in temas_subtemas}
    subtemas_map = {}
    for tema_key, subtemas in temas_subtemas.items():
        subtemas_map[tema_key.split(":")[0]] = {s.split(":")[0]: s for s in subtemas}
    return temas_map, subtemas_map

import re

def render_latex_response(solucion):
    """
    Render LaTeX-formatted explanation returned from the solver.
    Detects patterns like [ ... ] and displays them as LaTeX.
    """
    bloques = re.split(r"(\[.*?\])", solucion, flags=re.DOTALL)

    for bloque in bloques:
        if re.fullmatch(r"\[.*?\]", bloque.strip(), flags=re.DOTALL):
            # Strip brackets and show as LaTeX
            latex_code = bloque.strip()[1:-1]
            st.latex(latex_code)
        else:
            if bloque.strip():
                st.markdown(bloque.strip())


def main():
    st.set_page_config(page_title="Generador de Ejercicios 4º ESO", layout="centered")
    st.title("Generador Inteligente de Ejercicios de Matemáticas")
    st.markdown("¡Crea ejercicios personalizados para tus alumnos en segundos! ✨")
    st.markdown("---")

    # Preprocesamiento
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

    # GENERAR EJERCICIO
    if st.button("🚀 Generar Ejercicio", use_container_width=True):
        with st.spinner("Generando ejercicio..."):
            enunciado = new_func(tema, subtema, dificultad, tipo, perfil, detalles_adicionales)


        # Clean and transform the response into JSON
        try:
            enunciado = enunciado.replace("'", '"').replace("```json", "").replace("```", "")
            response_json = json.loads(enunciado)
            st.session_state["ultimo_enunciado"] = response_json.get("enunciado", "Error: 'enunciado' no encontrado en la respuesta.")
        except json.JSONDecodeError:
            st.error("Error al procesar la respuesta del modelo. Asegúrate de que sea un JSON válido.")
            st.session_state["ultimo_enunciado"] = "Error: No se pudo generar el enunciado."

        st.session_state["ultimo_tema"] = tema
        st.session_state["ultimo_subtema"] = subtema
        st.session_state["ultimo_perfil"] = perfil
        st.session_state["mostrar_solucion"] = False

    # MOSTRAR ENUNCIADO Y BOTÓN DE RESOLUCIÓN
    if "ultimo_enunciado" in st.session_state:
        st.subheader("📄 Enunciado")
        st.markdown(st.session_state["ultimo_enunciado"], unsafe_allow_html=True)

        # Botón de resolución
        if st.button("🧠 Ver Resolución Paso a Paso", use_container_width=True):
            st.session_state["mostrar_solucion"] = True

        # Mostrar resolución debajo
        if st.session_state.get("mostrar_solucion"):
            with st.spinner("Respondiendo con pasos detallados..."):
                solucion = solve_exercise(
                    st.session_state["ultimo_tema"],
                    st.session_state["ultimo_subtema"],
                    st.session_state["ultimo_enunciado"],
                    st.session_state["ultimo_perfil"]
                )

            # Clean and transform the response into JSON
            try:
                solucion = solucion.replace("'", '"').replace("```json", "").replace("```", "")
                response_json = json.loads(solucion)
                st.solucion = response_json.get("solucion", "Error: 'solucion' no encontrado en la respuesta.")
            except json.JSONDecodeError:
                st.error("Error al procesar la respuesta del modelo. Asegúrate de que sea un JSON válido.")
                solucion = "Error: No se pudo generar el solucion."
                
                st.markdown(solucion, unsafe_allow_html=True)
                st.subheader("🧩 Resolución Detallada")
                render_latex_response(solucion)

    st.markdown("---")
    st.caption("Desarrollado para prácticas del Máster en Formación del Profesorado · 2025")

def new_func(tema, subtema, dificultad, tipo, perfil, detalles_adicionales):
    enunciado = generate_exercise(tema, subtema, dificultad, tipo, perfil, detalles_adicionales)
    return enunciado

if __name__ == "__main__":
    main()
