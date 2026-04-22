from app.database.models import Patient, Visit, LabResult, VitalSign, Allergy


def get_patient_by_mrn(db, mrn: str):
    return db.query(Patient).filter(Patient.mrn == mrn).first()


def get_visits(db, patient_id):
    return db.query(Visit).filter(Visit.patient_id == patient_id).all()


def get_labs(db, patient_id):
    return db.query(LabResult).filter(LabResult.patient_id == patient_id).all()


def get_vitals(db, patient_id):
    return db.query(VitalSign).filter(VitalSign.patient_id == patient_id).all()


def get_allergies(db, patient_id):
    return db.query(Allergy).filter(Allergy.patient_id == patient_id).all()