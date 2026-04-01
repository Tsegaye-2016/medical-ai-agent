from app.services.ai_service import generate_response
from app.services.rag_service import retrieve_medical_context
from app.services.safety_service import check_emergency

def run_medical_agent(user_input: str):

    # 1. Safety check
    if check_emergency(user_input):
        return "⚠️ Emergency detected. Please go to a hospital immediately."

    # 2. Retrieve knowledge
    context = retrieve_medical_context(user_input)

    # 3. Build prompt
    prompt = f"""
    You are a clinical assistant.

    Rules:
    - Do NOT diagnose
    - Do NOT prescribe drugs
    - Provide educational information only

    Context:
    {context}

    Patient input:
    {user_input}

    Output:
    - Possible conditions
    - Explanation
    - When to see a doctor
    """

    # 4. Generate response
    response = generate_response(prompt)

    return response