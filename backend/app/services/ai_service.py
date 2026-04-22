# from langchain_ollama import ChatOllama
# from app.core.config import settings

# llm = ChatOllama(
#     model=settings.OLLAMA_MODEL,
#     base_url=settings.OLLAMA_BASE_URL,
#     temperature=settings.OLLAMA_TEMPERATURE
# )

# def generate_response(prompt: str):
#     return llm.invoke(prompt)
from langchain_ollama import ChatOllama
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(
    model=os.getenv("OLLAMA_MODEL"),
    base_url=os.getenv("OLLAMA_BASE_URL"),
    temperature=0.2
)


def generate_response(prompt: str):
    response = llm.invoke(prompt)
    return response.content