

# backend/schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HealthCheckResponse(BaseModel):
    pet_name: str
    status: str
    probable_disease: str
    treatment: Optional[str] = None



# ---------- Pet ----------
class PetCreate(BaseModel):
    name: str
    species: str
    breed: str
    owner_name: str
    owner_contact: str

class PetResponse(PetCreate):
    id: int
    class Config:
        from_attributes = True


# ---------- Appointment ----------
class AppointmentCreate(BaseModel):
    pet_name: str
    owner_name: Optional[str] = None
    date: Optional[str] = None
    time: Optional[str] = None
    doctor: Optional[str] = None
    emergency: Optional[bool] = False


class AppointmentResponse(BaseModel):
    id: int
    pet_name: str
    owner_name: str
    date: str
    time: str
    doctor: str
    emergency: bool
    status: str
    slot: str
    created_at: str


# ---------- Doctor ----------
class DoctorCreate(BaseModel):
    name: str
    specialty: str
    available: bool = True

class DoctorResponse(DoctorCreate):
    id: int
    class Config:
        from_attributes = True


# ---------- Staff ----------
class StaffCreate(BaseModel):
    name: str
    role: str
    present: bool = True

class StaffResponse(StaffCreate):
    id: int
    class Config:
        from_attributes = True


# ---------- Inventory ----------
class InventoryCreate(BaseModel):
    item: str
    quantity: int
    expiry: datetime

class InventoryResponse(InventoryCreate):
    id: int
    low_stock_flag: bool
    class Config:
        from_attributes = True
