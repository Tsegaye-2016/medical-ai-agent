from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.medical_agent import run_agent

router = APIRouter()

class Request(BaseModel):
    patient_id: str
    doctor_input: str

@router.post("/process")
def process(data: Request):
    return run_agent(data.patient_id, data.doctor_input)