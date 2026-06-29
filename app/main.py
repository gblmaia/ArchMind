from fastapi import FastAPI
from pydantic import BaseModel
import logging

# Importa a configuração de logs
from app.logging_config import setup_logging
from app.rag import ask_archmind

# Configura o logging
logger = setup_logging()

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
    logger.info(f"Nova pergunta recebida: {request.question}")

    try:
        resultado = ask_archmind(request.question)

        logger.info("Resposta gerada com sucesso")

        return ChatResponse(
            answer=resultado["answer"],
            sources=resultado["sources"]
        )

    except Exception as e:
        logger.error(f"Erro ao processar pergunta: {str(e)}")
        return ChatResponse(
            answer="Desculpe, ocorreu um erro ao processar sua pergunta.",
            sources=[]
        )