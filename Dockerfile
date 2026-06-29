# ============================================
# STAGE 1: Builder (instala dependências)
# ============================================
FROM python:3.11-slim AS builder

WORKDIR /app

# Instala dependências do sistema necessárias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements primeiro (melhor cache)
COPY requirements.txt .

# Instala dependências Python
RUN pip install --no-cache-dir --user -r requirements.txt

# ============================================
# STAGE 2: Runtime (imagem final menor)
# ============================================
FROM python:3.11-slim

WORKDIR /app

# Cria usuário não-root (segurança)
RUN useradd --create-home --shell /bin/bash appuser

# Copia as dependências instaladas do builder
COPY --from=builder /root/.local /home/appuser/.local

# Copia o código do projeto
COPY . .

# Ajusta permissões
RUN chown -R appuser:appuser /app

# Muda para o usuário não-root
USER appuser

# Adiciona o path das dependências instaladas
ENV PATH=/home/appuser/.local/bin:$PATH

# Expõe a porta do FastAPI
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]