from fastapi import FastAPI
from pydantic import BaseModel
import logging
import time

from app.logging_config import setup_logging
from app.rag import ask_archmind
from config import settings

logger = setup_logging()

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION
)

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[str] = []
    error: bool = False
    response_time: float = 0.0


@app.get("/")
def root():
    return {"message": "ArchMind API está rodando!"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    start_time = time.time()
    logger.info(f"Nova pergunta recebida: {request.question}")

    try:
        resultado = ask_archmind(request.question)
        elapsed = time.time() - start_time

        logger.info(f"Resposta gerada em {elapsed:.2f}s")

        return ChatResponse(
            answer=resultado["answer"],
            sources=resultado.get("sources", []),
            error=False,
            response_time=round(elapsed, 2)
        )

    except Exception as e:
        elapsed = time.time() - start_time
        logger.error(f"Erro após {elapsed:.2f}s: {str(e)}")

        return ChatResponse(
            answer="Desculpe, ocorreu um erro ao processar sua pergunta. Tente novamente mais tarde.",
            sources=[],
            error=True,
            response_time=round(elapsed, 2)
        )