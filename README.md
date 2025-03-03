# ChatBot-Sample

'''
Train dataset and save model 

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
'''

'''
docker build -t chat-bot .

docker run -itd -p 5000:5000 chat-bot 
'''