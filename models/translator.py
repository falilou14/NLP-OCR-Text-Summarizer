from transformers import MarianMTModel, MarianTokenizer
import streamlit as st

@st.cache_resource
def get_translator(target_lang: str = "fr"):
    """
    Charge et met en cache le modèle de traduction MarianMT.
    """
    if target_lang == "fr":
        model_name = "Helsinki-NLP/opus-mt-en-fr"
    else:
        model_name = "Helsinki-NLP/opus-mt-fr-en"

    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return model, tokenizer


def translate_text(model_tokenizer, text: str) -> str:
    """
    Traduit un texte avec le modèle et le tokenizer fournis.
    """
    model, tokenizer = model_tokenizer
    if not text.strip():
        return ""

    tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)
