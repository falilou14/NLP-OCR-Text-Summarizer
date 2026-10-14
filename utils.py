# utils.py
from PIL import Image
import pytesseract
import re
import os

# Si t'es sous Windows et que tesseract n'est pas dans le PATH,
# décommente et modifie le chemin ci-dessous :
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path: str, lang: str = "fra"):
    """
    Extrait du texte depuis une image via pytesseract.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang=lang)
        return text
    except Exception as e:
        return f"[Erreur OCR] {e}"

def clean_text(text: str) -> str:
    """
    Nettoyage de base : suppression d'espaces répétitifs, caractères bizarres,
    et coupe si très long (pour éviter d'envoyer trop gros au modèle).
    """
    if not text:
        return ""
    # supprimer null bytes etc.
    text = text.replace("\x00", " ")
    # normaliser espaces
    text = re.sub(r"\s+", " ", text).strip()
    # tronquer si trop long (ex : > 5000 chars)
    max_chars = 4000
    if len(text) > max_chars:
        text = text[:max_chars] + "..."
    return text
