import os
from openai import OpenAI
from dotenv import load_dotenv
import json
load_dotenv()  # Carga primero

# Obtiene la clave de entorno
api_key = os.getenv("OPENAI_API_KEY")

# Crea el cliente pasando la clave
client = OpenAI(api_key=api_key)

def call_gpt_4o(prompt, model="gpt-4o", temperature=1.0):
    """
    Llama a un modelo de OpenAI con el prompt dado.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Eres un generador de ejercicios de matemáticas para estudiantes de 4º de la ESO."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error en la llamada a GPT: {str(e)}"


def call_gpt_o3(prompt):
    """
    Llama específicamente a un modelo como gpt-3.5-turbo (puedes cambiar a otro O3-mini si lo conectas a través de una API local).
    """

    response = client.chat.completions.create(
        model="o3-mini",
        reasoning_effort="medium",
        messages=[
                {
                    "role": "user", 
                    "content": prompt
                }
            ]
        )
            
    return response.choices[0].message.content.strip()
