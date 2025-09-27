# streamlit_app.py
import streamlit as st
import requests
import uuid
import io
from PyPDF2 import PdfReader

st.set_page_config(page_title="LangGraph Chatbot", layout="centered")
st.title("💬 LangGraph Chatbot with PDF Support")

# Initialize session state
if "history" not in st.session_state:
    st.session_state["history"] = []
if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = str(uuid.uuid4())
if "document_text" not in st.session_state:
    st.session_state["document_text"] = ""

# Sidebar for file upload
with st.sidebar:
    st.header("📁 Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    if uploaded_file:
        try:
            reader = PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            st.session_state["document_text"] = text
            st.success("✅ PDF loaded!")
        except Exception as e:
            st.error(f"❌ Error reading PDF: {e}")
            st.session_state["document_text"] = ""

# Chat input
user_input = st.chat_input("Ask a question...")

if user_input:
    # Build context-aware message
    if st.session_state["document_text"]:
        full_query = (
            f"Use the following document to answer the question.\n\n"
            f"Document:\n{st.session_state['document_text'][:3000]}...\n\n"
            f"Question: {user_input}"
        )
    else:
        full_query = user_input

    # Append user message (show original question in UI)
    st.session_state["history"].append(("You", user_input))

    try:
        resp = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"user_message": full_query, "thread_id": st.session_state["thread_id"]},
            timeout=30  # longer timeout for document queries
        )
        resp.raise_for_status()
        bot_reply = resp.json()["response"]
    except Exception as e:
        bot_reply = f"⚠ Backend error: {e}"

    st.session_state["history"].append(("Bot", bot_reply))

# Display chat history
for sender, msg in st.session_state["history"]:
    with st.chat_message("user" if sender == "You" else "assistant"):
        st.markdown(msg)