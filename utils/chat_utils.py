# utils/chat_utils.py
import streamlit as st
from transformers import pipeline

HF_TOKEN = st.secrets.get("HF_TOKEN")
model_cache = {}

def load_model(model_name):
    if model_name not in model_cache:
        try:
            model_cache[model_name] = pipeline(
                "text-generation",
                model=model_name,
                token=HF_TOKEN,
                trust_remote_code=True
            )
        except OSError as e:
            st.error(f"❌ Failed to load model `{model_name}`: {e}")
            return None
    return model_cache[model_name]

def handle_user_query(prompt: str, model_name: str):
    model = load_model(model_name)
    if model is None:
        return "⚠️ Model not available. Check model name or Hugging Face token."
    output = model(prompt, max_new_tokens=256, do_sample=True)[0]['generated_text']
    return output.split(prompt)[-1].strip()
