# 🐾 AI Veterinary Hospital Management System

## Overview

The **AI Veterinary Hospital Management System** is a fully integrated solution for managing veterinary clinics, combining AI-powered pet health diagnostics, appointment scheduling, emergency handling, inventory management, doctor/staff management, and a multilingual chatbot for pet owners.  

This system demonstrates cutting-edge technologies such as **AI computer vision**, **FastAPI backend**, **Streamlit frontend**, and **real-time notifications**, making it a robust and impressive project for real-world applications.

---

## Features

### 1. 🩺 Animal Health Check
- Upload images of pets (dogs, cats, etc.).
- AI detects diseases and predicts severity.
- Provides treatment suggestions and prescriptions.
- Works for multiple types of diseases.
- Emergency detection triggers priority booking.

### 2. 📅 Appointment Management
- Book, reschedule, or cancel appointments.
- Standard and emergency appointments.
- Emergency appointments:
  - Checks doctor availability.
  - If unavailable, finds nearest hospital with the same doctor.
  - Sends alert messages to owner, doctor, and staff.
- Tracks appointment status and history.

### 3. 🏥 Emergency Handling
- AI-based detection of critical conditions triggers immediate action.
- Automatic routing to nearby hospitals if assigned doctor is unavailable.
- Sends notifications to all relevant stakeholders (owner, doctor, staff, inventory).

### 4. 🧑‍⚕️ Doctor & Staff Management
- Manage doctor specialties and availability.
- Track staff attendance and role-based access.
- Send notifications to doctors about upcoming appointments or emergencies.

### 5. 📦 Inventory Management
- Track medicine, vaccines, and medical resources.
- Auto-low-stock alerts.
- Prepare resources automatically for emergency cases.

### 6. 💬 Multilingual Chatbot
- Pet owners can ask questions about:
  - Diseases
  - Food recommendations
  - Appointments
- Bot responds in the same language as the query.
- Handles both general questions and health-specific advice.

### 7. 📊 Analytics Dashboard
- Visualize hospital metrics:
  - Disease trends
  - Revenue
  - Doctor performance
  - Inventory usage

### 8. 📌 Additional AI Features
- Predicts pet disease from image uploads.
- Detects emergency conditions.
- Suggests treatments and vaccinations.
- Provides owner-friendly notifications.

---

## Technologies Used

### Backend
- **FastAPI**: REST API for appointments, pets, doctors, inventory, and chatbot.
- **SQLAlchemy**: ORM for database models.
- **SQLite**: Simple and fast relational database.
- **Pydantic**: Data validation and schema definitions.

### Frontend
- **Streamlit**: User-friendly UI for pet owners and staff.
- Pages:
  - Health Check
  - Pets Management
  - Appointments
  - Doctors & Staff
  - Inventory
  - Chatbot

### AI/ML
- **Computer Vision**: Detect pet diseases from uploaded images.
- Emergency condition detection triggers alerts and priority booking.

### Notifications
- **Twilio or Email API**: Alerts for appointments and emergencies.
- Real-time staff and doctor notifications.

---

## Database Models

### Pets
- `id`, `name`, `species`, `breed`, `owner_name`, `owner_contact`
- Relationship with medical records.

### Doctors
- `id`, `name`, `specialty`, `available`

### Staff
- `id`, `name`, `role`, `present`

### Inventory
- `id`, `item`, `quantity`, `expiry`, `low_stock_flag`

### Appointments
- `id`, `pet_id`, `doctor_id`, `date`, `time`, `emergency`, `status`, `hospital_info`

### Medical Records
- `id`, `pet_id`, `diagnosis`, `treatment`, `prescription`, `created_at`

### Hospitals (for emergency routing)
- `id`, `name`, `address`, `latitude`, `longitude`, `doctors`

---

## API Endpoints

### Appointments
- `POST /api/appointments/book` → Book a standard appointment.
- `POST /api/appointments/emergency` → Book an emergency appointment.
- `GET /api/appointments/list` → List all appointments.

### Pets
- `POST /api/pets/add` → Add a new pet.
- `GET /api/pets/list` → List all pets.

### Inventory
- `GET /api/inventory/list` → View all inventory items.
- `POST /api/inventory/add` → Add inventory item.
- Auto alert when low stock.

### Health Check
- `POST /api/healthcheck/image` → Upload pet image for disease detection.

### Chatbot
- `POST /api/chatbot/ask` → Ask a question to multilingual chatbot.

---

## Setup Instructions

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python init_db.py  # Initialize database
uvicorn main:app --reload
ai-vet-system/
│
├── backend/
│   ├── main.py              # FastAPI entrypoint
│   ├── models.py            # Database models
│   ├── schemas.py           # Pydantic schemas
│   ├── routes/              # API route files
│   ├── database.py          # DB setup
│   └── init_db.py           # DB initialization
│
├── frontend/
│   ├── app.py               # Streamlit main app
│   ├── utils.py             # Helper functions (send_image, post_request)
│   ├── pages/               # Individual pages (health_check, pets, appointments, etc.)
│   └── ...                  # Static files
│
├── README.md
└── requirements.txt
How It Works

Pet owner logs in or visits the Streamlit frontend.

Uploads pet image for health check → AI predicts disease.

Book appointment (standard or emergency):

If emergency, system auto-checks doctor availability.

Finds nearby hospital if doctor unavailable.

Sends alerts to all stakeholders.

Inventory is automatically checked for necessary resources.

Staff and doctor dashboards update in real-time.

Multilingual chatbot helps owners with questions and guidance.

Admins can view analytics and track performance.

Potential Improvements

Integrate GPS tracking for pet owners heading to hospitals.

Connect real SMS/email API for real-time alerts.

Use a more advanced deep learning model for disease prediction.

Mobile-friendly Streamlit UI or React frontend for better user experience.

Conclusion

This project demonstrates a fully automated AI-powered veterinary hospital management system with:

AI disease detection

Emergency handling and routing

Appointment management

Doctor and staff management

Inventory monitoring

Multilingual chatbot support

It is a complete real-world solution for modern veterinary clinics, showcasing full-stack development, AI integration, and real-time operational features.
