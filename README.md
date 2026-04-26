🚀 Afrinex AI – Clinic Appointment API
> A scalable backend system for managing clinic patients and appointment scheduling, built with modern API design principles.

## Overview

This project is a RESTful API designed to manage healthcare clinic operations, including patient records and appointment scheduling. It demonstrates backend development skills such as API design, database integration, and data persistence.

## Key Features

👤 Patient management (create & retrieve patients)
📅 Appointment scheduling system
🔗 Relationship between patients and appointments
💾 Persistent storage using SQLite database
⚡ Fast and efficient API built with FastAPI
📄 Interactive API documentation via Swagger UI

## Tech Stack
Language: Python
Framework: FastAPI
Database: SQLite
ORM: SQLModel
Server: Uvicorn

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

## Future Improvements
Add authentication (JWT)
Validate patient existence before appointment creation
Add update & delete endpoints
Implement filtering (by date, department)
Deploy API to cloud (AWS / Render)

## About Afrinex AI
Afrinex AI focuses on building scalable AI and software solutions to improve healthcare, fintech, and business operations across Africa.

## Author
Moustapha Ilmi
Software Engineer | Data Analyst | Founder @ Afrinex AI
