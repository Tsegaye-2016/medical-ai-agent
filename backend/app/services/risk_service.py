HIGH_RISK = ["chest pain"]

def risk_score(symptoms):
    if any(s in HIGH_RISK for s in symptoms):
        return "high"
    return "low"