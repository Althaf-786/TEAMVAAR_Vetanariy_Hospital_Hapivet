# backend/routes/ehr.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import EHR

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE a new EHR record
@router.post("/")
def create_ehr(animal_name: str, owner_name: str, medical_history: str, db: Session = Depends(get_db)):
    ehr_record = EHR(
        animal_name=animal_name,
        owner_name=owner_name,
        medical_history=medical_history
    )
    db.add(ehr_record)
    db.commit()
    db.refresh(ehr_record)
    return {"status": "success", "ehr": ehr_record}

# READ all EHR records
@router.get("/")
def get_all_ehr(db: Session = Depends(get_db)):
    records = db.query(EHR).all()
    return {"status": "success", "ehr_records": records}

# READ a specific EHR record by ID
@router.get("/{ehr_id}")
def get_ehr(ehr_id: int, db: Session = Depends(get_db)):
    record = db.query(EHR).filter(EHR.id == ehr_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="EHR record not found")
    return {"status": "success", "ehr": record}

# UPDATE an existing EHR record
@router.put("/{ehr_id}")
def update_ehr(ehr_id: int, animal_name: str = None, owner_name: str = None, medical_history: str = None, db: Session = Depends(get_db)):
    record = db.query(EHR).filter(EHR.id == ehr_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="EHR record not found")
    
    if animal_name:
        record.animal_name = animal_name
    if owner_name:
        record.owner_name = owner_name
    if medical_history:
        record.medical_history = medical_history
    
    db.commit()
    db.refresh(record)
    return {"status": "success", "ehr": record}

# DELETE an EHR record
@router.delete("/{ehr_id}")
def delete_ehr(ehr_id: int, db: Session = Depends(get_db)):
    record = db.query(EHR).filter(EHR.id == ehr_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="EHR record not found")
    
    db.delete(record)
    db.commit()
    return {"status": "success", "message": f"EHR record {ehr_id} deleted"}

