from flask import Flask, request, jsonify, render_template
import pickle

# Load the pre-trained vectorizer and model
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "Please provide a question."}), 400
    question = data["question"]
    # Transform the input question
    X_test = vectorizer.transform([question])
    # Predict the answer
    predicted_answer = model.predict(X_test)[0]
    return jsonify({"answer": predicted_answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
