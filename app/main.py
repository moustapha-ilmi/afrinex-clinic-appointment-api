from fastapi import FastAPI
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional, List

app = FastAPI(
    title="Afrinex AI Clinic Appointment API",
    description="REST API for managing clinic patients and appointments.",
    version="1.0.0"
)

sqlite_file_name = "clinic.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)


class Patient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    gender: str


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.get("/")
def home():
    return {"message": "Afrinex AI Clinic Appointment API is running"}


@app.post("/patients", response_model=Patient)
def create_patient(patient: Patient):
    with Session(engine) as session:
        session.add(patient)
        session.commit()
        session.refresh(patient)
        return patient


@app.get("/patients", response_model=List[Patient])
def get_patients():
    with Session(engine) as session:
        patients = session.exec(select(Patient)).all()
        return patients

class Appointment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int
    department: str
    appointment_time: str
    status: str = "Scheduled"

# CREATE appointment
@app.post("/appointments", response_model=Appointment)
def create_appointment(appointment: Appointment):
    with Session(engine) as session:
        session.add(appointment)
        session.commit()
        session.refresh(appointment)
        return appointment


# GET all appointments
@app.get("/appointments", response_model=List[Appointment])
def get_appointments():
    with Session(engine) as session:
        appointments = session.exec(select(Appointment)).all()
        return appointments