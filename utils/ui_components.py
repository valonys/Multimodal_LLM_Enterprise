# utils/ui_components.py
import streamlit as st
from streamlit.components.v1 import html

USER_AVATAR = "https://cdn-icons-png.flaticon.com/512/456/456212.png"
BOT_AVATAR = "https://cdn-icons-png.flaticon.com/512/4712/4712107.png"

SEND_ICON = "\ud83d\udce4"
MIC_ICON = "\ud83c\udfa4"
PLUS_ICON = "\u2795"

def render_chat_interface():
    for role, message in st.session_state.chat_history:
        with st.chat_message(role, avatar=USER_AVATAR if role == "user" else BOT_AVATAR):
            st.markdown(message)

    st.markdown("""
    <style>
    .chat-icons {
        font-size: 1.4rem;
        display: flex;
        justify-content: end;
        gap: 1rem;
        margin-top: 0.5rem;
    }
    </style>
    <div class='chat-icons'>
        <span>{}</span>
        <span>{}</span>
        <span>{}</span>
    </div>
    """.format(PLUS_ICON, MIC_ICON, SEND_ICON), unsafe_allow_html=True)
