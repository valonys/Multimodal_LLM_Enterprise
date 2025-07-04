# utils/ui_components.py
import streamlit as st

USER_AVATAR = "https://cdn-icons-png.flaticon.com/512/456/456212.png"
BOT_AVATAR = "https://cdn-icons-png.flaticon.com/512/4712/4712107.png"

SEND_ICON = "📤"
MIC_ICON = "🎤"
PLUS_ICON = "➕"

def render_chat_interface():
    chat_history = st.session_state.get("chat_history", [])
    if not isinstance(chat_history, list):
        chat_history = []

    for role, message in chat_history:
        if role in ["user", "assistant"]:
            with st.chat_message(role, avatar=USER_AVATAR if role == "user" else BOT_AVATAR):
                st.markdown(str(message))

    st.markdown(f"""
    <style>
        .chat-icons {{
            font-size: 1.4rem;
            display: flex;
            justify-content: end;
            gap: 1rem;
            margin-top: 0.5rem;
        }}
    </style>
    <div class='chat-icons'>
        <span title="Upload">{PLUS_ICON}</span>
        <span title="Mic">{MIC_ICON}</span>
        <span title="Send">{SEND_ICON}</span>
    </div>
    """, unsafe_allow_html=True)