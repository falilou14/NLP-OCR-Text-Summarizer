# 🧠 NLP OCR Text Summarizer



## Description

**NLP OCR Text Summarizer** est une application web interactive qui permet de :

- Résumer des textes en français ou en anglais avec un pipeline NLP performant.
- Extraire du texte à partir d’images (OCR) et générer un résumé automatiquement.
- Traduire les résumés vers la langue souhaitée (français ou anglais).
- Stocker un historique des résumés pour consultation future.

Cette application est conçue pour être simple à utiliser et extensible pour d’autres projets NLP ou IA.

---

## 🛠️ Fonctionnalités

- Résumé automatique de texte
- Résumé de texte extrait d’images via OCR (Tesseract)
- Traduction automatique des résumés
- Historique des résumés
- Support multi-langue (FR / EN)
- Interface moderne avec Streamlit
- Compatible CPU/GPU (transformers et PyTorch)
- Bonus :
  - Analyse linguistique avec spaCy
  - Téléversement de fichiers TXT ou PDF
  - Déploiement possible comme API Flask pour réutilisation

---

## 🚀 Technologies utilisées

- Python 3.11+
- [Streamlit](https://streamlit.io/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [PyTorch](https://pytorch.org/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [spaCy](https://spacy.io/)
- SQLite pour la sauvegarde des résumés
- pandas pour la gestion des données

---

## ⚡ Installation

1. **Cloner le repo**
```bash
git clone https://github.com/falilou14/NLP-OCR-Text-Summarizer.git
cd NLP-OCR-Text-Summarizer

    Créer un environnement virtuel

python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Mac/Linux

    Installer les dépendances

pip install -r requirements.txt

    Installer Tesseract

    Télécharger et installer depuis : Tesseract OCR

    Ajouter le chemin de Tesseract dans les variables d’environnement (TESSDATA_PREFIX si nécessaire)

    Installer le modèle spaCy français

python -m spacy download fr_core_news_sm

🏃‍♂️ Utilisation

    Lancer l’application Streamlit :

streamlit run app.py

    Accéder à l’interface depuis le navigateur :
    http://localhost:8501

    Fonctions principales :

    Coller du texte pour générer un résumé

    Téléverser une image pour extraire le texte et résumer

    Choisir la langue de traduction

    Consulter l’historique des résumés

📁 Organisation du projet

NLP-OCR-Text-Summarizer/
│
├── app.py                 # Entrée principale de l’application Streamlit
├── models/
│   ├── summarizer.py      # Pipeline de résumé
│   └── translator.py      # Pipeline de traduction
├── utils.py               # Fonctions utilitaires (OCR, nettoyage)
├── database.py            # Gestion SQLite
├── requirements.txt       # Dépendances Python
├── README.md              # Documentation
└── venv/                  # Ne pas versionner !

💡 Conseils pour les recruteurs / utilisateurs

    L’application est extensible : tu peux ajouter de nouveaux modèles Transformers pour améliorer le résumé.

    Le projet peut être déployé sur Streamlit Cloud ou Render pour un accès web public.

    L’historique est stocké localement, mais peut être migré vers une base distante si besoin.

## 🔗 Liens utiles

- [Hugging Face Models](https://huggingface.co/models) — Collection de modèles NLP et Transformers  
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) — Outil open-source pour l’extraction de texte à partir d’images  
- [Streamlit Documentation](https://docs.streamlit.io/) — Documentation officielle Streamlit pour créer des apps interactives

