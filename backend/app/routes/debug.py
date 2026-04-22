from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.data_service import get_patient_by_mrn

router = APIRouter()

@router.get("/debug/{mrn}")
def debug_patient(mrn: str, db: Session = Depends(get_db)):
    patient = get_patient_by_mrn(db, mrn)

    if not patient:
        return {"error": "Not found"}

    return {
        "id": str(patient.id),
        "mrn": patient.mrn,
        "name": patient.full_name
    }