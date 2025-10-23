from typing import Dict
from random import choice

def predict_disease(image) -> Dict:
    diseases = ["Parvovirus", "Rabies", "Fleas", "Ticks", "Normal"]
    return {
        "pet_name": "Unknown",
        "status": "Critical" if choice([True, False]) else "Normal",
        "probable_disease": choice(diseases)
    }

