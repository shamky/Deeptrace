Here's the updated README file with the HTML part removed:

---

# Drug Suspicion Detection System

## Overview
This project is designed to detect suspicious drug-related activity in chat messages using **Natural Language Processing (NLP)**. 
It leverages a custom Named Entity Recognition (NER) model to identify drug-related terms, quantities, and actions. Additionally, 
the system flags messages that are suspicious based on predefined patterns.

## Features
- Detects drug names (e.g., meth, coke, LSD).
- Identifies quantities of drugs (e.g., grams, pills).
- Flags suspicious actions such as buying, selling, and delivering drugs.
- Custom NER model built with **spaCy** for entity recognition.
- Flask backend for processing and analyzing messages.

## Requirements

### Libraries Installed:
- **spaCy** - NLP library used for creating and running the custom NER model.
- **flask** - Web framework for building the backend.
- **flask-cors** - To allow cross-origin requests between frontend and backend.

### Python Version:
- Python 3.x (Recommended: Python 3.8 or higher)

### To install the required libraries, run:
```bash
pip install spacy flask flask-cors
```

### spaCy Model:
You will need to train and save the custom NER model in the `custom_ner_model` directory. You can use the `train_ner.py` script to train the model and then save it.

## Setup

1. **Clone the repository** or download the code to your local machine.
2. **Install dependencies** using the command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the Custom NER Model** using `train_ner.py` (if not already trained):
   ```bash
   python train_ner.py
   ```

4. **Run the Flask Backend**:
   Start the Flask server to handle API requests:
   ```bash
   python app.py
   ```

## How to Use

1. **Start the Flask Backend**:
   ```bash
   python app.py
   ```

2. **Analyze Messages**:
   Use the `analyze_message(message)` function in your code to send messages to the Flask API and get back results regarding the suspicious activity detected.

---
