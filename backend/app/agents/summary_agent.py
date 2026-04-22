from app.services.data_service import get_patient_by_mrn, get_visits, get_labs, get_vitals, get_allergies
from app.services.ai_service import generate_response
from app.utils.json_parser import safe_parse
def run_summary_agent(db, mrn: str):

    patient = get_patient_by_mrn(db, mrn)

    if not patient:
        return {"error": "Patient not found"}

    patient_id = patient.id

    visits = get_visits(db, patient_id)[-5:]
    labs = get_labs(db, patient_id)[-10:]
    vitals = get_vitals(db, patient_id)[-5:]
    allergies = get_allergies(db, patient_id)

    context = f"""
    Patient:
    Name: {patient.full_name}
    Gender: {patient.gender}
    DOB: {patient.dob}

    Visits:
    {[(v.visit_date, v.diagnosis) for v in visits]}

    Labs:
    {[ (l.test_name, l.value, l.normal_range, l.test_date) for l in labs ]}

    Vitals:
    {[ (v.systolic_bp, v.diastolic_bp, v.heart_rate, v.respiratory_rate, v.temperature, v.oxygen_saturation, v.notes) for v in vitals ]}

    Allergies:
    {[(a.allergy_name, a.reaction, a.severity) for a in allergies]}
    """

    # prompt = f"""
    # Summarize this patient and give:
    # - summary
    # - risks
    # - recommendations

    # Data:
    # {context}
    # """
    prompt = f"""
    You are a clinical AI assistant.

    Analyze the patient data and return ONLY valid JSON.

    DO NOT write explanations.
    DO NOT use markdown.
    DO NOT add text outside JSON.

    Return format:

    {{
    "summary": "short clinical summary",
    "key_findings": ["..."],
    "risks": ["..."],
    "recommendations": ["..."]
    }}

    Patient Data:
    {context}
    """
    # return generate_response(prompt)
    raw = generate_response(prompt)
    return safe_parse(raw)
