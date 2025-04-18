import spacy

# Load the trained model from disk
nlp = spacy.load("custom_ner_model")

# Test messages
test_texts = [
    "He just scored 2 grams of meth.",
    "Got 3 pills of ecstasy?",
    "Can you get weed for tomorrow?",
    "Let's meet after I grab 5 tabs of LSD.",
    "I'll bring 1 gram of heroin."
]

# Run the model on each text
for text in test_texts:
    doc = nlp(text)
    print(f"\nText: {text}")
    for ent in doc.ents:
        print(f"  → {ent.text} → {ent.label_}")
