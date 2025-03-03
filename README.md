# ChatBot Sample

## Overview
This is a simple chatbot implementation using a Naive Bayes classifier. The chatbot is trained on a small dataset of questions and answers, and it can respond to predefined questions based on the trained model.

## Features
- Uses `scikit-learn` for text vectorization and classification.
- Trains a Naive Bayes model on a small dataset.
- Saves the trained model and vectorizer as `.pkl` files for reuse.
- Deployable as a Docker container.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip
- Docker (if deploying with Docker)

### Install Required Dependencies
Run the following command to install necessary Python packages:
```bash
pip install scikit-learn
```

## Training the Model
The chatbot is trained using a small set of predefined questions and answers. The training script:
1. Vectorizes the input text using `CountVectorizer`.
2. Trains a Naive Bayes classifier (`MultinomialNB`).
3. Saves the trained model and vectorizer as `.pkl` files.

### Training Script
```python
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Define a small Q&A dataset
questions = [
    "How are you?",
    "What is your name?",
    "What time is it?",
    "How do you do?",
    "Where are you from?",
    "Tell me a joke."
]
answers = [
    "I am fine, thank you.",
    "My name is Chatbot.",
    "Time is an illusion.",
    "I am doing well.",
    "I come from a world of data.",
    "Why did the chicken cross the road? To get to the other side!"
]

# Vectorize the questions (convert text to numerical features)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(questions)

# Train a simple classifier
clf = MultinomialNB()
clf.fit(X, answers)

# Save the trained vectorizer and model to disk as .pkl files
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
with open("model.pkl", "wb") as f:
    pickle.dump(clf, f)

print("Model and vectorizer saved successfully.")
```

Run the training script:
```bash
python train.py
```
After running, `model.pkl` and `vectorizer.pkl` will be saved to the current directory.

## Running the Chatbot
To use the chatbot, load the trained model and vectorizer in a separate script or application that handles user input and responses.

## Docker Deployment
### Build the Docker Image
```bash
docker build -t chat-bot .
```

### Run the Docker Container
```bash
docker run -itd -p 5000:5000 chat-bot
```

## Future Improvements
- Expand the training dataset for better accuracy.
- Implement an API to handle chatbot queries dynamically.
- Use more advanced NLP models for improved responses.

## License
This project is open-source and can be modified and used freely.