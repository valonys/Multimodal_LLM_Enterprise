# utils/chat_utils.py
import os
from transformers import pipeline

# Load models
HF_TOKEN = os.getenv("HF_TOKEN")

def load_model(model_name):
    return pipeline("text-generation", model=model_name, token=HF_TOKEN)

llama4_model = load_model("llama4-scout")  # Replace with real model path
maverick_model = load_model("llama4-maverick")  # Replace with real model path
gemma_model = load_model("amiguel/gemma-3")

def handle_user_query(prompt: str):
    # Simple router (you can enhance this with UI selector later)
    model = gemma_model  # Default to gemma
    response = model(prompt, max_new_tokens=256, do_sample=True)[0]['generated_text']
    return response.split(prompt)[-1].strip()
