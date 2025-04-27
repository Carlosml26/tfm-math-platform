#!/bin/bash
set -e

SERVICE_NAME="math-gen"
REGION="europe-west1"

# Cargar variables de entorno desde .env si existe
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Comprobar que GOOGLE_CLOUD_PROJECT está definido
if [ -z "$GOOGLE_CLOUD_PROJECT" ]; then
    echo "❌ Error: La variable GOOGLE_CLOUD_PROJECT no está definida."
    exit 1
fi

IMAGE="gcr.io/$GOOGLE_CLOUD_PROJECT/$SERVICE_NAME:latest"

echo "🚀 Construyendo la imagen Docker..."
docker build -t $IMAGE .

echo "📤 Pusheando la imagen a Google Container Registry..."
docker push $IMAGE

echo "☁️ Desplegando en Cloud Run..."
gcloud run deploy $SERVICE_NAME \
  --image $IMAGE \
  --region $REGION \
  --platform managed \
  --allow-unauthenticated

echo "✅ Despliegue completado."

SERVICE_URL=$(gcloud run services describe $SERVICE_NAME \
    --platform managed \
    --region $REGION \
    --format 'value(status.url)')

echo "🌐 Tu servicio está disponible en: $SERVICE_URL"
