# src/services/llm/openai_connector.py

import os
import openai
from dotenv import load_dotenv

# Cargar credenciales de OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_openai(prompt: str, model="gpt-4", temperature=0.7) -> str:
    """Llama a la API de OpenAI GPT con el prompt dado."""
    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=1000
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"❌ Error en la llamada a OpenAI: {str(e)}"
