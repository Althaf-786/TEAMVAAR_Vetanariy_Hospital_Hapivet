# backend/routes/billing.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Billing

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE a new billing record
@router.post("/")
def create_billing(patient_name: str, amount: float, status: str = "Pending", db: Session = Depends(get_db)):
    billing_record = Billing(
        patient_name=patient_name,
        amount=amount,
        status=status
    )
    db.add(billing_record)
    db.commit()
    db.refresh(billing_record)
    return {"status": "success", "billing": billing_record}

# READ all billing records
@router.get("/")
def get_all_billing(db: Session = Depends(get_db)):
    records = db.query(Billing).all()
    return {"status": "success", "billing_records": records}

# READ a billing record by ID
@router.get("/{billing_id}")
def get_billing(billing_id: int, db: Session = Depends(get_db)):
    record = db.query(Billing).filter(Billing.id == billing_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Billing record not found")
    return {"status": "success", "billing": record}

# UPDATE a billing record
@router.put("/{billing_id}")
def update_billing(billing_id: int, patient_name: str = None, amount: float = None, status: str = None, db: Session = Depends(get_db)):
    record = db.query(Billing).filter(Billing.id == billing_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Billing record not found")
    
    if patient_name:
        record.patient_name = patient_name
    if amount is not None:
        record.amount = amount
    if status:
        record.status = status
    
    db.commit()
    db.refresh(record)
    return {"status": "success", "billing": record}

# DELETE a billing record
@router.delete("/{billing_id}")
def delete_billing(billing_id: int, db: Session = Depends(get_db)):
    record = db.query(Billing).filter(Billing.id == billing_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Billing record not found")
    
    db.delete(record)
    db.commit()
    return {"status": "success", "message": f"Billing record {billing_id} deleted"}

