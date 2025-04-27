# src/services/llm/provider.py

from enum import Enum, auto
from src.services.llm.openai_connector import call_openai
from src.services.llm.gemini_connector import call_gemini

class Provider(Enum):
    OPENAI = auto()
    GEMINI = auto()

def generate(prompt: str, provider: Provider = Provider.OPENAI) -> str:
    """Genera un enunciado o solución dependiendo del proveedor LLM."""
    if provider == Provider.OPENAI:
        return call_openai(prompt)
    elif provider == Provider.GEMINI:
        return call_gemini(prompt)
    else:
        raise ValueError("Proveedor LLM no soportado")
