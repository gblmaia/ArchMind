from langchain_community.llms import Ollama

# O cérebro agora está no seu PC, rodando na porta 11434
llm = Ollama(model="llama3.1")

def testar_conexao():
    print("Conectando ao cérebro local (Ollama)...")
    resposta = llm.invoke("Olá! Você está pronto para ser o cérebro do ArchMind?")
    print(f"Resposta: {resposta}")

if __name__ == "__main__":
    testar_conexao()