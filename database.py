# backend/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./vet_hospital.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# --- Mock in-memory lists for fast testing / prototype ---
appointments_db = []
pets_db = []
inventory_db = []
doctors_db = []
staff_db = []


# --- Dependency for FastAPI routes ---
def get_db():
    """
    Create a new database session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
