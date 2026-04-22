ABBREVIATIONS = {
    "dm": "diabetes",
    "sob": "shortness of breath"
}

def expand(text: str):
    for k, v in ABBREVIATIONS.items():
        text = text.replace(k, v)
    return text