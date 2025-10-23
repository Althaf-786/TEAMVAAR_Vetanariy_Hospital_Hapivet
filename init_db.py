from database import Base, engine
from models import Pet, Doctor, Staff, Inventory, Appointment

Base.metadata.create_all(bind=engine)
print("Database initialized ✅")
