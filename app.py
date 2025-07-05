# app.py
import streamlit as st
import os
from pathlib import Path
from dotenv import load_dotenv
from utils.chat_utils import handle_user_query
from utils.file_utils import handle_file_upload
from utils.ui_components import render_chat_interface
from streamlit.components.v1 import html

# Load secrets and config
load_dotenv()

# --- Page Setup ---
st.set_page_config(page_title="Enterprise Multimodal Agent", page_icon="💻", layout="wide")

# --- Session State Init ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "selected_model" not in st.session_state:
    st.session_state.selected_model = "amiguel/gemma-3"

# --- Sidebar ---
with st.sidebar:
    st.header("📄 Upload Files")
    uploaded_files = st.file_uploader("Upload .pdf, .xlsx, .docx, .ppt", accept_multiple_files=True,
                                      type=["pdf", "xlsx", "xls", "docx", "doc", "ppt", "pptx"])
    if uploaded_files:
        file_paths = handle_file_upload(uploaded_files)
        st.success(f"{len(file_paths)} file(s) processed.")

    st.markdown("---")
    st.subheader("🚀 Select Model")
    st.session_state.selected_model = st.selectbox(
        "Choose a model:",
        [
            "amiguel/gemma-3",
            "amiguel/GM_Qwen1.8B_Finetune",
            "meta-llama/Llama-4-Scout-17B-16E-Instruct",
            "meta-llama/Llama-4-Maverick-17B-128E-Instruct"
        ],
        index=0
    )

# --- Main Chat Interface ---
st.title("🧱 Enterprise Multimodal LLM Agent")
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/tw-cen-mt');
    html, body, [class*="css"]  { font-family: 'Tw Cen MT', sans-serif; }
    .stChatInputContainer textarea { min-height: 50px !important; }
    </style>
""", unsafe_allow_html=True)

# --- Render chat UI ---
render_chat_interface()

# --- Chat Handling ---
user_input = st.chat_input(placeholder="Ask about your documents or use voice (🎤)...", key="user_input")
if user_input:
    with st.spinner("Processing..."):
        response = handle_user_query(user_input, model_name=st.session_state.selected_model)
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("assistant", response))

# --- Microphone Voice Capture (JS) ---
st.markdown("---")
st.subheader("🎤 Voice Input (Experimental)")
html("""
<script>
  const button = document.createElement('button');
  button.textContent = '🎙️ Start Recording';
  button.style.fontSize = '1rem';
  document.body.appendChild(button);

  let recognition;
  if ('webkitSpeechRecognition' in window) {
    recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-US';

    button.onclick = () => {
      recognition.start();
    };

    recognition.onresult = function(event) {
      const transcript = event.results[0][0].transcript;
      const streamlitInput = window.parent.document.querySelector('[data-testid="stChatInput"] textarea');
      if (streamlitInput) {
        streamlitInput.value = transcript;
        streamlitInput.dispatchEvent(new Event('input', { bubbles: true }));
      }
    };
  } else {
    button.textContent = 'Speech Recognition not supported';
  }
</script>
""", height=100)
