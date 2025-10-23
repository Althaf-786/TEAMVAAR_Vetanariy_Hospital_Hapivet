from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    species = Column(String)
    breed = Column(String)
    owner_name = Column(String)
    owner_contact = Column(String)
    medical_records = relationship("MedicalRecord", back_populates="pet")

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    specialty = Column(String)
    available = Column(Boolean, default=True)

class Staff(Base):
    __tablename__ = "staff"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)
    present = Column(Boolean, default=True)

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String)
    quantity = Column(Integer)
    expiry = Column(DateTime)
    low_stock_flag = Column(Boolean, default=False)

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, ForeignKey("pets.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    date = Column(DateTime, default=datetime.utcnow)
    emergency = Column(Boolean, default=False)
    status = Column(String, default="Scheduled")
    pet = relationship("Pet")
    doctor = relationship("Doctor")

class MedicalRecord(Base):
    __tablename__ = "medical_records"
    id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, ForeignKey("pets.id"))
    diagnosis = Column(String)
    treatment = Column(String)
    prescription = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    pet = relationship("Pet", back_populates="medical_records")

# backend/models.py

class Hospital(Base):
    __tablename__ = "hospitals"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    doctors = relationship("Doctor", back_populates="hospitals")

Doctor.hospitals = relationship("Hospital", secondary="doctor_hospital", back_populates="doctors")

class DoctorHospital(Base):
    __tablename__ = "doctor_hospital"
    doctor_id = Column(Integer, ForeignKey("doctors.id"), primary_key=True)
    hospital_id = Column(Integer, ForeignKey("hospitals.id"), primary_key=True)

