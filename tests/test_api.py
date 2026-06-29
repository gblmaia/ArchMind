from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    """Testa se o endpoint raiz está funcionando."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "ArchMind API está rodando!"}


def test_chat_endpoint():
    """Testa o endpoint /chat com uma pergunta simples."""
    response = client.post(
        "/chat",
        json={"question": "Qual é o nome do projeto?"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "sources" in data
    assert isinstance(data["answer"], str)