# # app.py
# import os
# import streamlit as st
# from models.summarizer import get_summarizer, summarize_text
# from models.translator import get_translator, translate_text
# from utils import extract_text_from_image, clean_text
# from database import init_db, save_summary, get_all_summaries
# import pandas as pd
# from datetime import datetime

# # Configuration page
# st.set_page_config(page_title="Résumé Intelligent", layout="wide")
# st.title("🧠 Résumeur de texte & image — Avec traduction et historique")

# # Init DB
# init_db()

# # Load models (cached)
# summarizer = get_summarizer()          # pipeline de résumé
# translator_en_fr, translator_fr_en = get_translator()  # pipelines de traduction

# # Sidebar : options globales
# st.sidebar.header("Options globales")
# theme = st.sidebar.radio("Thème", ["Sombre", "Clair"])
# # (Le thème global peut aussi être réglé via .streamlit/config.toml)

# st.sidebar.markdown("---")
# st.sidebar.header("Paramètres du résumé")
# max_len = st.sidebar.slider("Longueur max du résumé", 30, 300, 120)
# min_len = st.sidebar.slider("Longueur min du résumé", 10, 25, 25)

# st.sidebar.markdown("---")
# st.sidebar.header("Langue")
# target_lang = st.sidebar.selectbox("Langue de sortie (traduction)", ["None", "fr", "en"])

# # Main UI: onglets
# tab = st.tabs(["Résumé de texte", "Résumé d'image (OCR)", "Historique"])

# # ----- PAGE 1 : Résumé de texte -----
# with tab[0]:
#     st.header("✍️ Résumer un texte")
#     text_input = st.text_area("Colle ton texte ici :", height=250)

#     col1, col2 = st.columns([1, 1])
#     with col1:
#         if st.button("Générer le résumé"):
#             if not text_input.strip():
#                 st.warning("Merci d'entrer du texte.")
#             else:
#                 with st.spinner("Génération du résumé..."):
#                     cleaned = clean_text(text_input)
#                     summary = summarize_text(summarizer, cleaned, max_length=max_len, min_length=min_len)
#                     st.subheader("Résumé")
#                     st.write(summary)

#                     translated = None
#                     if target_lang != "None":
#                         with st.spinner("Traduction..."):
#                             if target_lang == "fr":
#                                 translated = translate_text(translator_en_fr, summary)
#                             else:
#                                 translated = translate_text(translator_fr_en, summary)
#                             st.subheader(f"Traduction ({target_lang})")
#                             st.write(translated)

#                     # Sauvegarde
#                     save_summary(text_input, summary, translated)
#                     st.success("Résumé sauvegardé dans l'historique ✅")

#     with col2:
#         st.info("Conseils d'utilisation")
#         st.markdown("""
#         - Pour de meilleurs résultats, fournis des blocs de texte cohérents (paragraphes).
#         - Si le texte est trop long, la fonction le tronquera automatiquement.
#         - Tu peux changer la longueur du résumé et la langue de sortie depuis la barre latérale.
#         """)

# # ----- PAGE 2 : Résumé d'image (OCR) -----
# with tab[1]:
#     st.header("🖼️ Résumer une image (OCR)")
#     uploaded_file = st.file_uploader("Téléverse une image (png, jpg, jpeg)", type=["png", "jpg", "jpeg"])
#     if uploaded_file:
#         st.image(uploaded_file, caption="Image téléchargée", use_column_width=True)
#         if st.button("Extraire le texte & résumer"):
#             with st.spinner("Extraction du texte (OCR)..."):
#                 # save temp
#                 tmp_path = "temp_uploaded_image.png"
#                 with open(tmp_path, "wb") as f:
#                     f.write(uploaded_file.getbuffer())

#                 extracted = extract_text_from_image(tmp_path)
#                 st.subheader("Texte extrait")
#                 st.write(extracted)

#                 if not extracted.strip():
#                     st.warning("Aucun texte détecté dans l'image.")
#                 else:
#                     with st.spinner("Génération du résumé..."):
#                         cleaned = clean_text(extracted)
#                         summary = summarize_text(summarizer, cleaned, max_length=max_len, min_length=min_len)
#                         st.subheader("Résumé")
#                         st.write(summary)

#                         translated = None
#                         if target_lang != "None":
#                             with st.spinner("Traduction..."):
#                                 if target_lang == "fr":
#                                     translated = translate_text(translator_en_fr, summary)
#                                 else:
#                                     translated = translate_text(translator_fr_en, summary)
#                                 st.subheader(f"Traduction ({target_lang})")
#                                 st.write(translated)

#                         save_summary(extracted, summary, translated)
#                         st.success("Résumé (OCR) sauvegardé ✅")

# # ----- PAGE 3 : Historique -----
# with tab[2]:
#     st.header("🗂️ Historique des résumés")
#     rows = get_all_summaries()
#     if not rows:
#         st.info("Aucun résumé en base. Génère un résumé pour en créer un.")
#     else:
#         df = pd.DataFrame(rows, columns=["id", "text", "summary", "translated", "date"])
#         # show preview
#         st.dataframe(df[["id", "summary", "translated", "date"]])

#         st.markdown("### Visualiser un résumé")
#         sel = st.number_input("Entrer l'id du résumé à afficher", min_value=1, max_value=int(df["id"].max()), step=1)
#         if st.button("Afficher l'historique"):
#             sel_row = df[df["id"] == sel]
#             if sel_row.empty:
#                 st.warning("ID non trouvé.")
#             else:
#                 row = sel_row.iloc[0]
#                 st.subheader("Texte original")
#                 st.write(row["text"])
#                 st.subheader("Résumé")
#                 st.write(row["summary"])
#                 if row["translated"]:
#                     st.subheader("Traduction")
#                     st.write(row["translated"])
#                 st.write(f"🔖 Date : {row['date']}")

# # Footer
# st.markdown("---")
# st.caption("App by FALILOU — utilise transformers, pytesseract et sqlite pour un workflow simple et pratique.")



# # app.py
# import os
# import streamlit as st
# from models.summarizer import get_summarizer, summarize_text
# from models.translator import get_translator, translate_text

# from utils import extract_text_from_image, clean_text
# from database import init_db, save_summary, get_all_summaries
# import pandas as pd

# # --- CONFIGURATION DE LA PAGE ---
# st.set_page_config(page_title="Résumé Intelligent", layout="wide")
# st.title("🧠 Résumeur de texte & image — Avec traduction et historique")

# # --- INITIALISATION BASE DE DONNÉES ---
# init_db()

# # --- CHARGEMENT DU PIPELINE (mis en cache) ---
# summarizer = get_summarizer()  # pipeline résumé

# # --- SIDEBAR ---
# st.sidebar.header("Options globales")
# theme_choice = st.sidebar.radio("Thème", ["Sombre", "Clair"])

# # --- CSS DYNAMIQUE POUR THÈME ---
# if theme_choice == "Sombre":
#     primary_color = "#FF4B4B"
#     background_color = "#0E1117"
#     secondary_background = "#262730"
#     text_color = "#FAFAFA"
# else:
#     primary_color = "#FF4B4B"
#     background_color = "#FAFAFA"
#     secondary_background = "#F0F2F6"
#     text_color = "#0E1117"

# st.markdown(
#     f"""
#     <style>
#     /* Fond principal et textes */
#     .stApp {{
#         background-color: {background_color};
#         color: {text_color};
#     }}
#     /* Sidebar */
#     .css-1d391kg {{
#         background-color: {secondary_background};
#     }}
#     /* Textarea */
#     .stTextArea>div>div>textarea {{
#         background-color: {secondary_background};
#         color: {text_color};
#     }}
#     /* Buttons */
#     .stButton>button {{
#         background-color: {primary_color};
#         color: {text_color};
#         border: none;
#     }}
#     /* Sliders */
#     .stSlider>div {{
#         background-color: {secondary_background};
#         color: {text_color};
#     }}
#     /* Radios */
#     .stRadio>div {{
#         background-color: {secondary_background};
#         color: {text_color};
#     }}
#     /* Selectbox */
#     .stSelectbox>div {{
#         background-color: {secondary_background};
#         color: {text_color};
#     }}
#     /* File uploader */
#     .stFileUploader>div {{
#         background-color: {secondary_background};
#         color: {text_color};
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # --- PARAMÈTRES DU RÉSUMÉ ---
# st.sidebar.markdown("---")
# st.sidebar.header("Paramètres du résumé")
# max_len = st.sidebar.slider("Longueur max du résumé", 30, 300, 120)
# min_len = st.sidebar.slider("Longueur min du résumé", 10, 25, 25)

# # --- LANGUE DE TRADUCTION ---
# st.sidebar.markdown("---")
# st.sidebar.header("Langue")
# target_lang = st.sidebar.selectbox("Langue de sortie (traduction)", ["None", "fr", "en"])

# # --- ONGLETS ---
# tab = st.tabs(["Résumé de texte", "Résumé d'image (OCR)", "Historique"])

# # ----- PAGE 1 : Résumé de texte -----
# with tab[0]:
#     st.header("✍️ Résumer un texte")
#     text_input = st.text_area("Colle ton texte ici :", height=250)

#     col1, col2 = st.columns([1, 1])
#     with col1:
#         if st.button("Générer le résumé"):
#             if not text_input.strip():
#                 st.warning("Merci d'entrer du texte.")
#             else:
#                 with st.spinner("Génération du résumé..."):
#                     cleaned = clean_text(text_input)
#                     summary = summarize_text(summarizer, cleaned)
#                     st.subheader("Résumé")
#                     st.write(summary)

#                     translated = None
                    
#                     if target_lang != "None":
#                         with st.spinner("Traduction..."):
#                             if target_lang == "fr":
#                                 translator_en_fr = get_translator("fr")
#                                 translated = translate_text(translator_en_fr, summary)
#                             else:
#                                 translator_fr_en = get_translator("en")
#                                 translated = translate_text(translator_fr_en, summary)
#                             st.subheader(f"Traduction ({target_lang})")
#                             st.write(translated)

#                     save_summary(text_input, summary, translated)
#                     st.success("Résumé sauvegardé dans l'historique ✅")

#     with col2:
#         st.info("Conseils d'utilisation")
#         st.markdown("""
#         - Pour de meilleurs résultats, fournis des blocs de texte cohérents (paragraphes).
#         - Si le texte est trop long, la fonction le tronquera automatiquement.
#         - Tu peux changer la langue de sortie depuis la barre latérale.
#         """)

# # ----- PAGE 2 : Résumé d'image (OCR) -----
# with tab[1]:
#     st.header("🖼️ Résumer une image (OCR)")
#     uploaded_file = st.file_uploader("Téléverse une image (png, jpg, jpeg)", type=["png", "jpg", "jpeg"])
#     if uploaded_file:
#         st.image(uploaded_file, caption="Image téléchargée", use_column_width=True)
#         if st.button("Extraire le texte & résumer"):
#             with st.spinner("Extraction du texte (OCR)..."):
#                 tmp_path = "temp_uploaded_image.png"
#                 with open(tmp_path, "wb") as f:
#                     f.write(uploaded_file.getbuffer())

#                 extracted = extract_text_from_image(tmp_path)
#                 st.subheader("Texte extrait")
#                 st.write(extracted)

#                 if not extracted.strip():
#                     st.warning("Aucun texte détecté dans l'image.")
#                 else:
#                     with st.spinner("Génération du résumé..."):
#                         cleaned = clean_text(extracted)
#                         summary = summarize_text(summarizer, cleaned)
#                         st.subheader("Résumé")
#                         st.write(summary)

#                         translated = None
#                         if target_lang != "None":
#                             with st.spinner("Traduction..."):
#                                 translated = translate_summary(summary, target_lang)
#                                 st.subheader(f"Traduction ({target_lang})")
#                                 st.write(translated)

#                         save_summary(extracted, summary, translated)
#                         st.success("Résumé (OCR) sauvegardé ✅")

# # ----- PAGE 3 : Historique -----
# with tab[2]:
#     st.header("🗂️ Historique des résumés")
#     rows = get_all_summaries()
#     if not rows:
#         st.info("Aucun résumé en base. Génère un résumé pour en créer un.")
#     else:
#         df = pd.DataFrame(rows, columns=["id", "text", "summary", "translated", "date"])
#         st.dataframe(df[["id", "summary", "translated", "date"]])

#         st.markdown("### Visualiser un résumé")
#         sel = st.number_input("Entrer l'id du résumé à afficher", min_value=1, max_value=int(df["id"].max()), step=1)
#         if st.button("Afficher l'historique"):
#             sel_row = df[df["id"] == sel]
#             if sel_row.empty:
#                 st.warning("ID non trouvé.")
#             else:
#                 row = sel_row.iloc[0]
#                 st.subheader("Texte original")
#                 st.write(row["text"])
#                 st.subheader("Résumé")
#                 st.write(row["summary"])
#                 if row["translated"]:
#                     st.subheader("Traduction")
#                     st.write(row["translated"])
#                 st.write(f"🔖 Date : {row['date']}")

# # --- FOOTER ---
# st.markdown("---")
# st.caption("App by FALILOU — utilise transformers, pytesseract et sqlite pour un workflow simple et pratique.")




# app.py
import os
import streamlit as st
from models.summarizer import get_summarizer, summarize_text
from models.translator import get_translator, translate_text
from utils import extract_text_from_image, clean_text
from database import init_db, save_summary, get_all_summaries
import pandas as pd
import spacy
import PyPDF2
# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Résumé Intelligent", layout="wide")
st.title(" Résumeur de texte & image — Avec traduction et historique")

# --- INITIALISATION BASE DE DONNÉES ---
init_db()

# --- CHARGEMENT DU PIPELINE (mis en cache) ---
summarizer = get_summarizer()

# --- SIDEBAR ---
st.sidebar.header("Options globales")
theme_choice = st.sidebar.radio("Thème", ["Sombre", "Clair"])

# --- CSS DYNAMIQUE POUR THÈME ---
if theme_choice == "Sombre":
    primary_color = "#FF4B4B"
    background_color = "#0E1117"
    secondary_background = "#262730"
    text_color = "#FAFAFA"
else:
    primary_color = "#FF4B4B"
    background_color = "#FAFAFA"
    secondary_background = "#F0F2F6"
    text_color = "#0E1117"

st.markdown(
    f"""
    <style>
    /* Fond principal et textes */
    .stApp {{
        background-color: {background_color};
        color: {text_color};
    }}
    /* Sidebar */
    .css-1d391kg {{
        background-color: {secondary_background};
    }}
    /* Textarea */
    .stTextArea>div>div>textarea {{
        background-color: {secondary_background};
        color: {text_color};
        border-radius: 6px;
    }}
    /* Buttons */
    .stButton>button {{
        background-color: {primary_color};
        color: #FFFFFF;
        border-radius: 8px;
        font-weight: bold;
        padding: 0.5rem 1rem;
    }}
    .stButton>button:hover {{
        background-color: #e03d3d;
    }}
    /* Sliders */
    .stSlider>div {{
        background-color: {secondary_background};
        color: {text_color};
    }}
    /* Radios */
    .stRadio>div {{
        background-color: {secondary_background};
        color: {text_color};
    }}
    /* Selectbox */
    .stSelectbox>div {{
        background-color: {secondary_background};
        color: {text_color};
    }}
    /* File uploader */
    .stFileUploader>div {{
        background-color: {secondary_background};
        color: {text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- PARAMÈTRES DU RÉSUMÉ ---
st.sidebar.markdown("---")
st.sidebar.header("Paramètres du résumé")
max_len = st.sidebar.slider("Longueur max du résumé", 30, 300, 120)
min_len = st.sidebar.slider("Longueur min du résumé", 10, 25, 25)

# --- LANGUE DE TRADUCTION ---
st.sidebar.markdown("---")
st.sidebar.header("Langue")
target_lang = st.sidebar.selectbox("Langue de sortie (traduction)", ["None", "fr", "en"])

# --- INITIALISATION spaCy ---
nlp = spacy.load("fr_core_news_sm")

# --- ONGLETS ---
tab = st.tabs(["Résumé de texte", "Résumé d'image (OCR)", "Historique"])

# ----- PAGE 1 : Résumé de texte -----
with tab[0]:
    st.header("✍️ Résumer un texte ou fichier")
    
    # --- TELEVERSEMENT DE FICHIERS ---
    uploaded_file = st.file_uploader("📄 Téléverse un fichier texte ou PDF", type=["txt", "pdf"])
    text_input = ""
    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text_input = "\n".join([page.extract_text() for page in pdf_reader.pages])
        else:
            text_input = str(uploaded_file.read(), "utf-8")
        st.info("Texte extrait du fichier chargé.")

    # --- Textarea ---
    if not text_input:
        text_input = st.text_area("Colle ton texte ici :", height=250)
    else:
        st.text_area("Texte à résumer :", value=text_input, height=250)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Générer le résumé"):
            if not text_input.strip():
                st.warning("Merci d'entrer du texte ou de téléverser un fichier.")
            else:
                cleaned = clean_text(text_input)

                # --- ANALYSE NLP ---
                doc = nlp(cleaned)
                sentences = [sent.text for sent in doc.sents]
                st.write(f"Nombre de phrases détectées : {len(sentences)}")
                st.write("Exemples de phrases :", sentences[:5])

                # --- GENERATION DU RESUME ---
                with st.spinner("Génération du résumé..."):
                    summary = summarize_text(summarizer, cleaned)
                    st.subheader("Résumé")
                    st.write(summary)

                    translated = None
                    if target_lang != "None":
                        with st.spinner("Traduction..."):
                            if target_lang == "fr":
                                translator_en_fr = get_translator("fr")
                                translated = translate_text(translator_en_fr, summary)
                            else:
                                translator_fr_en = get_translator("en")
                                translated = translate_text(translator_fr_en, summary)
                            st.subheader(f"Traduction ({target_lang})")
                            st.write(translated)

                    save_summary(text_input, summary, translated)
                    st.success("Résumé sauvegardé dans l'historique ✅")

    with col2:
        st.info("Conseils d'utilisation")
        st.markdown("""
        - Pour de meilleurs résultats, fournis des blocs de texte cohérents.
        - Tu peux téléverser un fichier texte ou PDF pour résumer automatiquement.
        - Tu peux changer la langue de sortie depuis la barre latérale.
        """)

# ----- PAGE 2 : Résumé d'image (OCR) -----
with tab[1]:
    st.header("🖼️ Résumer une image (OCR)")
    uploaded_image = st.file_uploader("Téléverse une image (png, jpg, jpeg)", type=["png", "jpg", "jpeg"])
    if uploaded_image:
        st.image(uploaded_image, caption="Image téléchargée", use_column_width=True)
        if st.button("Extraire le texte & résumer"):
            with st.spinner("Extraction du texte (OCR)..."):
                tmp_path = "temp_uploaded_image.png"
                with open(tmp_path, "wb") as f:
                    f.write(uploaded_image.getbuffer())

                extracted = extract_text_from_image(tmp_path)
                st.subheader("Texte extrait")
                st.write(extracted)

                if extracted.strip():
                    with st.spinner("Génération du résumé..."):
                        cleaned = clean_text(extracted)
                        summary = summarize_text(summarizer, cleaned)
                        st.subheader("Résumé")
                        st.write(summary)

                        translated = None
                        if target_lang != "None":
                            with st.spinner("Traduction..."):
                                if target_lang == "fr":
                                    translator_en_fr = get_translator("fr")
                                    translated = translate_text(translator_en_fr, summary)
                                else:
                                    translator_fr_en = get_translator("en")
                                    translated = translate_text(translator_fr_en, summary)
                                st.subheader(f"Traduction ({target_lang})")
                                st.write(translated)

                        save_summary(extracted, summary, translated)
                        st.success("Résumé (OCR) sauvegardé ✅")
                else:
                    st.warning("Aucun texte détecté dans l'image.")

# ----- PAGE 3 : Historique -----
with tab[2]:
    st.header("🗂️ Historique des résumés")
    rows = get_all_summaries()
    if not rows:
        st.info("Aucun résumé en base. Génère un résumé pour en créer un.")
    else:
        df = pd.DataFrame(rows, columns=["id", "text", "summary", "translated", "date"])
        st.dataframe(df[["id", "summary", "translated", "date"]])

        st.markdown("### Visualiser un résumé")
        sel = st.number_input("Entrer l'id du résumé à afficher", min_value=1, max_value=int(df["id"].max()), step=1)
        if st.button("Afficher l'historique"):
            sel_row = df[df["id"] == sel]
            if sel_row.empty:
                st.warning("ID non trouvé.")
            else:
                row = sel_row.iloc[0]
                st.subheader("Texte original")
                st.write(row["text"])
                st.subheader("Résumé")
                st.write(row["summary"])
                if row["translated"]:
                    st.subheader("Traduction")
                    st.write(row["translated"])
                st.write(f"🔖 Date : {row['date']}")

# --- FOOTER ---
st.markdown("---")
st.caption("App by FALILOU")
