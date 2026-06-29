FROM python:3.11-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Instala algumas ferramentas do sistema que o ChromaDB precisa
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de dependências primeiro (isso ajuda a Docker usar cache)
COPY requirements.txt .

# Instala as bibliotecas do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o resto do projeto para dentro do container
COPY . .

# Cria a pasta do ChromaDB (caso não exista)
RUN mkdir -p chroma_db

# Comando que vai rodar quando o container iniciar
CMD ["python", "main.py"]