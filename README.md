# ArchMind

Assistente de mentoria e onboarding técnico baseado em **RAG (Retrieval-Augmented Generation)** local.

O ArchMind foi desenvolvido para eliminar a fragmentação de conhecimento corporativo, permitindo que novos desenvolvedores consultem manuais, regras de negócio e arquitetura de forma rápida e precisa, sem depender exclusivamente de Tech Leads.

## ✨ Funcionalidades

- RAG 100% local (sem depender de APIs externas)
- Utiliza **Llama 3.1** via Ollama
- Banco vetorial **ChromaDB**
- Prompts otimizados para respostas técnicas precisas
- Suporte a tabelas e extração exata de informações
- Pipeline de ingestão profissional (estilo enterprise)

## 🛠 Tecnologias

- Python 3.11+
- LangChain (Classic)
- Ollama + Llama 3.1
- ChromaDB
- HuggingFace Embeddings (all-MiniLM-L6-v2)
- PyPDFLoader + RecursiveCharacterTextSplitter

## 📁 Estrutura do Projeto

```text
archmind/
├── data/
│   └── docs/              # Coloque seus PDFs aqui
├── chroma_db/             # Banco vetorial gerado (ignorado no Git)
├── ingestion.py           # Script de ingestão de documentos
├── main.py                # Interface de chat RAG
├── requirements.txt
├── .env
└── .gitignore

```

## 🚀 Como executar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```
### 2. Iniciar o Ollama
Certifique-se que o Ollama está rodando e que o modelo está baixado:

```bash
ollama serve
ollama pull llama3.1
```
### 3. Fazer a ingestão dos documentos
Coloque seus arquivos .pdf dentro da pasta data/docs/ e rode:

```bash
python ingestion.py
```
### 4. Iniciar o ArchMind

```bash
Bashpython main.py
```
Depois é só fazer perguntas normalmente. Para sair digite sair, exit ou quit.

## ⚠️ Observações Importantes

A pasta chroma_db/ não deve ser commitada (já está no .gitignore)
Documentos sensíveis ou PDFs devem ficar na pasta data/docs/
O sistema responde apenas com base no contexto ingerido. Se não encontrar a informação, ele avisa.
Temperatura do modelo está em 0 para maior precisão factual.

## 📌 Status
Projeto em desenvolvimento.
Versão atual: RAG 1.0 (pipeline local enterprise)
