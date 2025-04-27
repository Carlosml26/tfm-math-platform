# src/core/generator.py

from config.prompts import render_prompt

def generate_exercise(tema, subtema, dificultad, tipo, perfil, detalles_adicionales):
    """
    Genera un enunciado para el ejercicio, usando la plantilla de Jinja2.
    """
    prompt_text = render_prompt(
        "exercise.prompt.j2",  # Nombre de la plantilla
        {
            "tema": tema,
            "subtema": subtema,
            "dificultad": dificultad,
            "tipo": tipo,
            "perfil": perfil,
            "detalles": detalles_adicionales
        }
    )
    return prompt_text
