# models/summarizer.py
from transformers import pipeline
import os
import streamlit as st

# Utiliser un modèle plus léger par défaut (évite les gros téléchargements)
DEFAULT_MODEL = "sshleifer/distilbart-cnn-12-6"

@st.cache_resource
def get_summarizer(model_name: str = DEFAULT_MODEL):
    """
    Retourne un pipeline de résumé (mis en cache par Streamlit).
    Change le model_name si tu veux un modèle plus lourd/performant.
    """
    os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
    summarizer = pipeline("summarization", model=model_name)
    return summarizer

# def summarize_text(summarizer, text: str, max_length: int = 120, min_length: int = 25):
#     """
#     Appelle le pipeline de résumé et renvoie la chaîne de résumé.
#     """
#     # HuggingFace met parfois en garde sur la longueur -> on peut chunker si besoin (ici simple)
#     if len(text.strip()) == 0:
#         return ""
#     # Le pipeline peut attendre une liste ou un string
#     result = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
#     return result[0]["summary_text"]


def summarize_text(summarizer, text: str):
    text = text.strip()
    if not text:
        return "⚠️ Texte vide."

    # On compte la longueur en tokens approximativement (nombre de mots)
    length = len(text.split())

    # Règles dynamiques : ajuster min/max_length selon la taille du texte
    if length < 30:
        return text  # trop court pour être résumé
    elif length < 100:
        max_length = 50
        min_length = 15
    elif length < 300:
        max_length = 120
        min_length = 30
    else:
        max_length = 180
        min_length = 50

    # Appel du modèle
    result = summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False,
    )
    return result[0]["summary_text"]
