from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import Pet
from backend.schemas import PetCreate, PetResponse

router = APIRouter(prefix="/pets", tags=["Pets"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PetResponse)
def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    db_pet = Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

@router.get("/", response_model=list[PetResponse])
def list_pets(db: Session = Depends(get_db)):
    return db.query(Pet).all()
