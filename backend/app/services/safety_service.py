EMERGENCY_KEYWORDS = [
    "chest pain",
    "can't breathe",
    "severe bleeding",
    "unconscious"
]

def check_emergency(text: str):
    for word in EMERGENCY_KEYWORDS:
        if word in text.lower():
            return True
    return False