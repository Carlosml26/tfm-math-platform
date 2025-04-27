# src/services/llm/gemini_connector.py

import os
from google import genai
from google.genai.types import HttpOptions

PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
MODEL_ID = os.getenv("GEMINI_MODEL", "gemini-2.0-flash-001")

def call_gemini(prompt: str, model: str = MODEL_ID, temperature: float = 0.7) -> str:
    """Llama al modelo Gemini de Google Cloud."""
    genai.configure(project=PROJECT, location=LOCATION)
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        generation_config={"temperature": temperature},
    )
    return response.text.strip()
