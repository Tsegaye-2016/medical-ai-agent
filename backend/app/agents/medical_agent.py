from app.services.emr_service import get_patient_history
from app.services.nlp_service import extract_symptoms
from app.services.risk_service import risk_score
from app.services.abbreviation_service import expand
from app.services.ai_service import generate_response
from app.services.rag_service import retrieve_medical_context
from app.services.safety_service import check_emergency


def run_agent(patient_id: str, doctor_input: str):

    # 1. Expand abbreviations
    text = expand(doctor_input)

    # 2. Emergency check
    if check_emergency(text):
        return {"emergency": True}

    # 3. History
    history = get_patient_history(patient_id)

    # 4. Symptoms
    symptoms = extract_symptoms(text)

    # 5. Risk
    risk = risk_score(symptoms)

    # 6. Context
    context = retrieve_medical_context(text)

    # 7. Prompt
    prompt = f"""
    Patient History: {history}
    Symptoms: {symptoms}
    Risk: {risk}

    Input: {text}

    Return JSON:
    {{
      "clinical_note": "...",
      "recommendations": []
    }}
    """

    # 8. AI
    ai_output = generate_response(prompt)

    return {
        "symptoms": symptoms,
        "risk": risk,
        "ai_output": ai_output
    }