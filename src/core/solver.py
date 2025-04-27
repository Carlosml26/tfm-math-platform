# src/core/solver.py

from config.prompts import render_prompt
from src.services.llm.openai_connector import call_gpt_o3
import json

def solve_exercise(tema, subtema, enunciado, perfil):
    """
    Genera la solución paso a paso usando LaTeX, con base en el enunciado proporcionado.
    """
    solution_prompt = render_prompt(
        "solution.prompt.j2",
        {
            "tema": tema,
            "subtema": subtema,
            "enunciado": enunciado,
            "perfil": perfil
        }
    )

    # Llamar al proveedor LLM para generar la solución
    generated_solution = call_gpt_o3(solution_prompt)

    return generated_solution
