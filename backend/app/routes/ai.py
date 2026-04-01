from fastapi import APIRouter
from app.agents.medical_agent import run_medical_agent

router = APIRouter()

@router.post("/ask")
def ask_ai(question: str):
    response = run_medical_agent(question)
    return {"response": response}