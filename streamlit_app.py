import streamlit as st
from app.rag import ask_archmind
import time

# ==================== CONFIGURAÇÃO DA PÁGINA ====================
st.set_page_config(
    page_title="ArchMind",
    page_icon="🦊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== SIDEBAR PROFISSIONAL ====================
with st.sidebar:
    st.title("🦊 ArchMind")
    st.markdown("**Assistente Técnico Inteligente**")
    st.caption("Powered by RAG • LangChain • FastAPI")

    st.divider()

    st.markdown("### 📌 Sobre o Projeto")
    st.markdown("""
    Sistema de **Retrieval-Augmented Generation (RAG)** desenvolvido para 
    consultas técnicas em documentação corporativa.
    """)

    st.divider()

    with st.expander("🛠️ Stack Tecnológica", expanded=False):
        st.markdown("""
        - **Backend**: FastAPI + Python
        - **RAG**: LangChain + ChromaDB
        - **LLM**: Ollama (Llama 3.1)
        - **Interface**: Streamlit
        - **Infra**: Docker + Pydantic Settings
        """)

    st.divider()

    st.markdown("### 📊 Status")
    st.success("Sistema operacional", icon="✅")

    st.divider()
    st.caption("Desenvolvido por **Gabriel Alves** • 2026")

# ==================== CABEÇALHO PRINCIPAL ====================
st.title("🦊 ArchMind")
st.caption("Assistente Técnico com RAG • Métricas de desempenho em tempo real")

st.divider()

# ==================== HISTÓRICO DE MENSAGENS ====================
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    avatar = "🧑‍💻" if message["role"] == "user" else "🦊"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# ==================== INPUT DO USUÁRIO ====================
if prompt := st.chat_input("Faça uma pergunta sobre a documentação técnica..."):
    # Adiciona mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(prompt)

    # Gera resposta do assistente
    with st.chat_message("assistant", avatar="🦊"):
        with st.spinner("Consultando base de conhecimento..."):
            start_time = time.time()
            resultado = ask_archmind(prompt)
            elapsed = time.time() - start_time

            resposta = resultado["answer"]
            sources = resultado.get("sources", [])

            # Monta resposta final
            resposta_final = resposta
            if sources:
                resposta_final += "\n\n**📚 Fontes consultadas:**\n"
                for s in sources:
                    resposta_final += f"- `{s}`\n"

            # Exibe métricas
            col1, col2 = st.columns([3, 1])
            with col1:
                st.caption(f"⏱️ **Respondido em {elapsed:.2f}s**")
            with col2:
                st.caption(f"📄 {len(sources)} fonte(s) utilizada(s)")

            st.markdown(resposta_final)

    # Salva no histórico
    st.session_state.messages.append({"role": "assistant", "content": resposta_final})