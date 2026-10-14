import spacy

# Charger le modèle français
nlp = spacy.load("fr_core_news_sm")

# Exemple de texte
texte = "Emmanuel Macron est le président de la France."

# Analyse
doc = nlp(texte)

for ent in doc.ents:
    print(ent.text, ent.label_)
