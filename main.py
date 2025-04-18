import spacy
# import os

# Load the custom NER model
nlp = spacy.load("custom_ner_model")

# Define suspicious keywords (optional)
suspicious_keywords = ["get", "buy", "sell", "score", "deliver", "hook", "stash"]

# Load chat data
with open('sample_data/chat_sample.txt', 'r', encoding='utf-8') as f:
    chat_lines = [line.strip() for line in f.readlines() if line.strip()]

print("=== Analyzing Messages ===\n")

for idx, message in enumerate(chat_lines):
    doc = nlp(message)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    matched_drugs = [ent.text for ent in doc.ents if ent.label_ == "DRUG"]
    matched_quantities = [ent.text for ent in doc.ents if ent.label_ == "QUANTITY"]
    matched_actions = [
        ent.text for ent in doc.ents if ent.label_ == "ACTION"
    ] + [
        word for word in message.lower().split() if word in suspicious_keywords
    ]

    is_suspicious = bool(matched_drugs or matched_actions)

    if is_suspicious:
        print(f"[SUSPICIOUS] Message {idx + 1}: {message}")
        if matched_drugs:
            print(f"  → Matched drugs: {matched_drugs}")
        if matched_quantities:
            print(f"  → Matched quantities: {matched_quantities}")
        if matched_actions:
            print(f"  → Matched actions: {matched_actions}")
        if entities:
            print(f"  → Entities: {entities}")
        print()
    else:
        print(f"Message {idx + 1}: {message}")
        if entities:
            print(f"  → Entities: {entities}")
        print()
