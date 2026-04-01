from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3",
    temperature=0.2
)

def generate_response(prompt: str):
    return llm.invoke(prompt)