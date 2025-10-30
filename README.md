# 🧠 NLP OCR Text Summarizer

## 🎯 Objectif
Application de traitement automatique du langage (NLP) permettant :
- d’extraire le texte à partir d’images ou de documents PDF (OCR),
- de générer automatiquement un résumé cohérent en français ou en anglais.

## ⚙️ Technologies utilisées
- **Python 3.10+**
- **Flask / Streamlit**
- **Tesseract OCR**
- **Hugging Face Transformers (T5, BART)**
- **OpenCV, Pillow**
- **SpaCy**

## 🚀 Fonctionnalités
- Upload d’image ou de PDF
- Extraction automatique du texte via Tesseract
- Résumé intelligent avec modèles de NLP pré-entraînés
- Interface simple et intuitive
- Multilingue (FR / EN)

## 🧩 Architecture

## 📸 Exemple
| Entrée (image) | Sortie (texte résumé) |
|----------------|-----------------------|
| ![sample](samples/example.png) | "Le document présente un résumé des principales tendances..." |

## 🧑‍💻 Installation
```bash
git clone https://github.com/ton-utilisateur/NLP-OCR-Text-Summarizer.git
cd NLP-OCR-Text-Summarizer
pip install -r requirements.txt
python app.py
