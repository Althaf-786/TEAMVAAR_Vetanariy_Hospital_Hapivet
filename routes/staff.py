from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import Staff

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add staff
@router.post("/")
def add_staff(name: str, role: str, present: bool = True, db: Session = Depends(get_db)):
    staff = Staff(name=name, role=role, present=present)
    db.add(staff)
    db.commit()
    db.refresh(staff)
    return {"message": "Staff added", "staff_id": staff.id}

# Get staff
@router.get("/")
def get_staff(db: Session = Depends(get_db)):
    return db.query(Staff).all()

