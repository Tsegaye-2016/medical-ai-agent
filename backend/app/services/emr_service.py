import requests
from app.core.config import settings

headers = {
    "Authorization": f"Bearer {settings.EMR_TOKEN}"
}

def get_patient_history(patient_id: str):
    response = requests.get(
        f"{settings.EMR_BASE_URL}/patients/{patient_id}/visits",
        headers=headers,
        timeout=settings.EMR_TIMEOUT
    )
    return response.json()