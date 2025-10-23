# backend/routes/appointments.py
from fastapi import APIRouter, HTTPException
from backend.schemas import AppointmentCreate, AppointmentResponse
from backend.database import appointments_db, doctors_db, hospitals_db
from datetime import datetime

router = APIRouter(prefix="/api/appointments", tags=["Appointments"])

@router.post("/emergency", response_model=AppointmentResponse)
async def emergency_booking(appointment: AppointmentCreate):
    """
    Book an emergency appointment.
    Checks doctor availability and nearby hospitals if needed.
    """
    try:
        # 1️⃣ Validate input
        if not appointment.pet_name:
            raise HTTPException(status_code=400, detail="Pet name is required")

        # 2️⃣ Find doctor availability
        doctor = next((d for d in doctors_db if d["name"] == appointment.doctor), None)
        if not doctor or not doctor["available"]:
            # 3️⃣ Find nearby hospital with available doctor
            nearby_hospital = next(
                (h for h in hospitals_db if appointment.doctor in h["doctors"]), None
            )
            if nearby_hospital:
                # Send alert messages
                # (In production, integrate Twilio / email / push notification)
                print(f"Emergency! Pet {appointment.pet_name} should go to {nearby_hospital['name']} at {nearby_hospital['address']}")
                hospital_info = f"{nearby_hospital['name']}, {nearby_hospital['address']}"
            else:
                hospital_info = "No nearby hospital found. Please contact admin."
        else:
            hospital_info = "Your doctor is available at the main hospital."

        # 4️⃣ Create appointment
        new_appointment = {
            "id": len(appointments_db) + 1,
            "pet_name": appointment.pet_name,
            "owner_name": appointment.owner_name,
            "date": datetime.utcnow().isoformat(),
            "time": "Immediate",
            "doctor": appointment.doctor,
            "emergency": True,
            "status": "Emergency Confirmed",
            "hospital_info": hospital_info,
            "created_at": datetime.utcnow().isoformat()
        }

        appointments_db.append(new_appointment)
        return new_appointment

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error booking emergency appointment: {e}")
