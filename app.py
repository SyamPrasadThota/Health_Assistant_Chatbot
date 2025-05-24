from flask import Flask, request, render_template
import numpy as np
import pickle
import json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load model and preprocessing objects
model = load_model('chat_model.h5')
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)
with open('label_encoder.pkl', 'rb') as enc:
    lbl_encoder = pickle.load(enc)

with open('intents.json') as file:
    data = json.load(file)

# Settings
max_len = 20

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form.get("msg", "")
    print("Received message:", msg)

    if msg.strip() == "":
        return "Please enter a message."

    # Preprocess input
    sequence = tokenizer.texts_to_sequences([msg])
    padded = pad_sequences(sequence, truncating='post', maxlen=max_len)
    
    # Predict
    pred = model.predict(padded)[0]
    tag = lbl_encoder.inverse_transform([np.argmax(pred)])[0]

    # Find response
    for intent in data['intents']:
        if intent['tag'] == tag:
            response = np.random.choice(intent['responses'])
            print("Response:", response)
            return response

    return "Sorry, I didn't understand that."

if __name__ == "__main__":
    app.run(debug=True)
