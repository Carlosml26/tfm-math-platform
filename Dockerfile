# syntax=docker/dockerfile:1
FROM python:3.10-slim

ENV POETRY_VERSION=1.8.2 \
    PYTHONUNBUFFERED=1 \
    PORT=8080        

# Dependencias del sistema mínimas
RUN apt-get update && apt-get install -y build-essential curl && \
    rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /app

EXPOSE 8080
ENTRYPOINT ["poetry", "run", "streamlit", "run", "src/app/webapp.py", \
            "--server.port=8080", "--server.address=0.0.0.0"]

