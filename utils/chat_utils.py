# utils/chat_utils.py
import streamlit as st
from transformers import pipeline

HF_TOKEN = st.secrets["HF_TOKEN"]

model_cache = {}

def load_model(model_name):
    if model_name not in model_cache:
        model_cache[model_name] = pipeline(
            "text-generation",
            model=model_name,
            token=HF_TOKEN,
            trust_remote_code=True
        )
    return model_cache[model_name]

def handle_user_query(prompt: str, model_name: str):
    model = load_model(model_name)
    output = model(prompt, max_new_tokens=256, do_sample=True)[0]['generated_text']
    return output.split(prompt)[-1].strip()
