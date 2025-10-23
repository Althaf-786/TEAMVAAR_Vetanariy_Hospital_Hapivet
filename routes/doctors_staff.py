from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import Doctor, Staff
from backend.schemas import (
    DoctorCreate, DoctorResponse,
    StaffCreate, StaffResponse
)

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------- DOCTORS ----------

@router.post("/add_doctor", response_model=DoctorResponse)
def add_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    new_doctor = Doctor(**doctor.dict())
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor

@router.get("/list_doctors", response_model=list[DoctorResponse])
def list_doctors(db: Session = Depends(get_db)):
    return db.query(Doctor).all()

@router.put("/update_doctor/{doctor_id}", response_model=DoctorResponse)
def update_doctor(doctor_id: int, updated: DoctorCreate, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise Exception("Doctor not found")
    for key, value in updated.dict().items():
        setattr(doctor, key, value)
    db.commit()
    db.refresh(doctor)
    return doctor


# ---------- STAFF ----------

@router.post("/add_staff", response_model=StaffResponse)
def add_staff(staff: StaffCreate, db: Session = Depends(get_db)):
    new_staff = Staff(**staff.dict())
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff

@router.get("/list_staff", response_model=list[StaffResponse])
def list_staff(db: Session = Depends(get_db)):
    return db.query(Staff).all()

@router.put("/update_staff/{staff_id}", response_model=StaffResponse)
def update_staff(staff_id: int, updated: StaffCreate, db: Session = Depends(get_db)):
    staff = db.query(Staff).filter(Staff.id == staff_id).first()
    if not staff:
        raise Exception("Staff not found")
    for key, value in updated.dict().items():
        setattr(staff, key, value)
    db.commit()
    db.refresh(staff)
    return staff
