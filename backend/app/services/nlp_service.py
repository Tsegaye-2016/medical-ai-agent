SYMPTOMS = ["fever", "cough", "chest pain", "dizziness"]

def extract_symptoms(text: str):
    return [s for s in SYMPTOMS if s in text.lower()]