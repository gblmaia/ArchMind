from langchain_ollama import OllamaLLM
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# ==================== CONFIGURAÇÕES ====================
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
llm = OllamaLLM(model="llama3.1", temperature=0)

vector_db = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)
retriever = vector_db.as_retriever(search_kwargs={"k": 5})

# ==================== PROMPT  ====================
prompt = ChatPromptTemplate.from_template("""
Você é um engenheiro de software sênior com vasta experiência em arquitetura e boas práticas.
Responda à pergunta do usuário **usando apenas o contexto fornecido**.

Regras importantes:
- Se a informação estiver em tabela, leia a tabela completa e extraia os dados de forma precisa.
- NÃO invente nem infira informações que não estejam explicitamente no contexto.
- Se não souber a resposta com base no contexto, diga claramente que não encontrou a informação.
- Seja técnico, direto e objetivo.

CONTEXTO:
{context}

PERGUNTA: {input}
""")

document_chain = create_stuff_documents_chain(llm, prompt)
qa_chain = create_retrieval_chain(retriever, document_chain)

# ==================== INTERFACE ====================
print("--- ArchMind Online (Enterprise RAG) ---")

while True:
    pergunta = input("\nVocê: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("ArchMind: Até mais, humano~")
        break

    resposta = qa_chain.invoke({"input": pergunta})
    print(f"\nArchMind:\n{resposta['answer']}")