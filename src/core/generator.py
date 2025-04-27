# src/core/generator.py

from config.prompts import render_prompt
from src.services.llm.openai_connector import call_gpt_4o

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

    # Llamar al proveedor LLM para generar el enunciado
    generated_exercise = call_gpt_4o(prompt_text)
    
    return generated_exercise
