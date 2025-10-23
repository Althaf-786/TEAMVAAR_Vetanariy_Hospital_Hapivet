from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import healthcheck, appointments, pets, doctors_staff, inventory, chatbot

app = FastAPI(title="AI Vet System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(healthcheck.router)
app.include_router(appointments.router)
app.include_router(pets.router)
app.include_router(doctors_staff.router)
app.include_router(inventory.router)
app.include_router(chatbot.router)

@app.get("/")
def root():
    return {"message": "AI Vet System backend running!"}
