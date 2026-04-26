🚀 Afrinex AI – Clinic Appointment API

A production-style backend system for managing clinic patients and appointment scheduling, built with scalable API design and database integration.

## Overview
This project simulates a real-world healthcare backend system, designed to manage patient records and appointment scheduling efficiently.
It demonstrates core backend engineering skills:

REST API design
Data modeling & persistence
System scalability thinking
Clean and maintainable architecture

🧠 System Architecture
Client (Browser / Postman)
        ↓
 FastAPI (REST API Layer)
        ↓
   SQLModel (ORM)
        ↓
     SQLite DB

## Key Features
👤 Patient management (create & retrieve)
📅 Appointment scheduling system
🔗 Patient–Appointment relationship
💾 Persistent storage with SQLite
⚡ High-performance API using FastAPI
📄 Auto-generated API docs (Swagger UI)

## Tech Stack
Layer	      Technology
Backend	      Python, FastAPI|
ORM	      SQLModel
Database      SQLite
Server	      Uvicorn|

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API home |
| POST | `/patients` | Create patient |
| GET | `/patients` | List patients |
| POST | `/appointments` | Create appointment |
| GET | `/appointments` | List appointments |

## Running the Project Locally
1. Clone the repository
git clone https://github.com/moustapha-ilmi/afrinex-clinic-appointment-api.git
cd afrinex-clinic-appointment-api
2. Install dependencies
pip3 install -r requirements.txt
3. Run the API
python3 -m uvicorn app.main:app --reload
4. Open API Docs

Visit:
http://127.0.0.1:8000/docs

## Example Request

Create Patient

{
  "name": "Moustapha Ilmi",
  "age": 25,
  "gender": "Male"
}

Create Appointment

{
  "patient_id": 1,
  "department": "General Medicine",
  "appointment_time": "2026-02-01 10:00",
  "status": "Scheduled"
}

## Future Improvements
Add authentication (JWT)
Validate patient existence before appointment creation
Add update & delete endpoints
Implement filtering (by date, department)
Deploy API to cloud (AWS / Render)

## What This Project Demonstrates

Designing RESTful APIs
Working with relational databases
Managing data persistence
Structuring backend applications
Building scalable, real-world systems

## About Afrinex AI
Afrinex AI focuses on building scalable AI and software solutions to improve healthcare, fintech, and business operations across Africa.

## Author
Moustapha Ilmi
Software Engineer | Data Analyst | Founder @ Afrinex AI
