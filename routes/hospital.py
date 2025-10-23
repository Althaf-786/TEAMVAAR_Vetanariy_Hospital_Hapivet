# backend/routes/hospital.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal, Appointment, Billing, Inventory, EHR

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/appointments")
def list_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()
