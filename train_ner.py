import spacy
from spacy.training.example import Example

# STEP 1: Create a blank English NLP pipeline
nlp = spacy.blank("en")

# STEP 2: Add the NER component
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner")

# STEP 3: Add custom entity labels
labels = ["DRUG", "QUANTITY", "ACTION"]
for label in labels:
    ner.add_label(label)

# STEP 4: Define training data
TRAIN_DATA = [
    ("Got 3 grams of meth?", {"entities": [(4, 13, "QUANTITY"), (17, 21, "DRUG")]}),
    ("Can you score some weed for me?", {"entities": [(12, 17, "ACTION"), (22, 26, "DRUG")]}),
    ("I'll bring the acid tonight.", {"entities": [(14, 18, "DRUG")]}),
    ("He wants 5 tabs of LSD.", {"entities": [(9, 18, "QUANTITY"), (22, 25, "DRUG")]}),
    ("You got the stuff?", {"entities": [(8, 13, "DRUG")]}),
    ("I can deliver 2 grams of heroin later.", {"entities": [(7, 14, "ACTION"), (15, 26, "QUANTITY"), (30, 36, "DRUG")]}),
    ("Need 10 pills of ecstasy by 6pm.", {"entities": [(5, 16, "QUANTITY"), (20, 27, "DRUG")]}),
    ("Got some shrooms?", {"entities": [(9, 16, "DRUG")]}),
    ("He’s holding 4 ounces of weed.", {"entities": [(12, 24, "QUANTITY"), (28, 32, "DRUG")]}),
    ("Do you have ketamine?", {"entities": [(12, 20, "DRUG")]}),
    ("She can hook us up with some coke.", {"entities": [(9, 21, "ACTION"), (32, 36, "DRUG")]}),
    ("I’ll get a bag of hash for you.", {"entities": [(5, 8, "ACTION"), (14, 18, "DRUG")]}),
    ("They asked for 6 grams of crack.", {"entities": [(15, 26, "QUANTITY"), (30, 35, "DRUG")]}),
    ("He’s dealing 2 grams of speed daily.", {"entities": [(6, 13, "ACTION"), (14, 25, "QUANTITY"), (29, 34, "DRUG")]}),
    ("Gonna need 5 packs of LSD.", {"entities": [(11, 21, "QUANTITY"), (25, 28, "DRUG")]}),
]

# STEP 5: Training loop
optimizer = nlp.begin_training()
for i in range(30):
    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], sgd=optimizer)

# STEP 6: Save the model
nlp.to_disk("custom_ner_model")
print("✅ Custom NER model trained and saved to 'ner_model/'")
