# Afrinex AI – Clinic Appointment API

A REST API for managing clinic patients and appointments, built with FastAPI and SQLite.

## Features
- Create and list patients
- Create and list appointments
- Store data in SQLite database
- Auto-generated API documentation with Swagger UI

## Tech Stack
- Python
- FastAPI
- SQLModel
- SQLite
- Uvicorn

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API home |
| POST | `/patients` | Create patient |
| GET | `/patients` | List patients |
| POST | `/appointments` | Create appointment |
| GET | `/appointments` | List appointments |

## Run Locally

```bash
pip3 install -r requirements.txt
python3 -m uvicorn app.main:app --reload