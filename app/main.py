from fastapi import FastAPI
from pydantic import BaseModel

# Importa a função que criamos no rag.py
from app.rag import ask_archmind

app = FastAPI(title="ArchMind API", version="1.0")


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[str] = []


@app.get("/")
def root():
    return {"message": "ArchMind API está rodando!"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Aqui chamamos o RAG de verdade
    resultado = ask_archmind(request.question)

    return ChatResponse(
        answer=resultado["answer"],
        sources=resultado["sources"]
    )