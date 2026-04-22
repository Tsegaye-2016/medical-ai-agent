from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.agents.summary_agent import run_summary_agent

router = APIRouter()


@router.get("/summary/{mrn}")
def summary(mrn: str, db: Session = Depends(get_db)):
    return run_summary_agent(db, mrn)