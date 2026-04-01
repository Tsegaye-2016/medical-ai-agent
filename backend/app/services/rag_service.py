from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding
)

def retrieve_medical_context(query: str):
    docs = vector_db.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])