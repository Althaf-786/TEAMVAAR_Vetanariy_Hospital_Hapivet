# backend/routes/healthcheck.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.schemas import HealthCheckResponse
import random
import shutil
import os

router = APIRouter(prefix="/api/healthcheck", tags=["Health Check"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/image", response_model=HealthCheckResponse)
async def analyze_health(image: UploadFile = File(...)):
    """
    Analyze uploaded pet image and predict health status or disease.
    """
    try:
        file_path = os.path.join(UPLOAD_DIR, image.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        # Simulate AI model prediction (you can plug your real model here)
        diseases = ["Healthy", "Skin Infection", "Allergy", "Ear Infection", "Eye Issue", "Fever"]
        disease = random.choice(diseases)
        status = "Normal" if disease == "Healthy" else "Needs Attention"

        # Mock treatment recommendation
        treatment = {
            "Healthy": "No treatment needed. Keep monitoring.",
            "Skin Infection": "Apply antiseptic ointment and keep area dry.",
            "Allergy": "Consult vet, possible antihistamine prescribed.",
            "Ear Infection": "Clean ears daily and apply antibiotic drops.",
            "Eye Issue": "Use prescribed eye drops, avoid dust.",
            "Fever": "Provide fluids, consult vet if persists >24h."
        }

        result = HealthCheckResponse(
            pet_name="Unknown",
            status=status,
            probable_disease=disease,
            treatment=treatment[disease]
        )

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {e}")
