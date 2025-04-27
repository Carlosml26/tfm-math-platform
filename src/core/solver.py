# src/core/solver.py

from config.prompts import render_prompt

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
    return solution_prompt
