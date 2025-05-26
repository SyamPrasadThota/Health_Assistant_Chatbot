
# AI Chatbot with Deep Learning

This is an AI-powered chatbot built using deep learning techniques and deployed via a Flask web interface. The chatbot can understand and respond to user queries based on predefined intents using a trained neural network model.

---

## 🤖 Features

- Deep learning–based intent classification
- Clean and interactive web interface
- Trainable on custom intents (`intents.json`)
- Persistent tokenization and label encoding
- Lightweight Flask app for local deployment

---

## ✅ Prerequisites

- Python 3.8+
- pip (Python package manager)
- Basic knowledge of machine learning (for retraining, optional)

---

## ⚙️ Installation

1. **Clone the repository**:
```bash
git clone https://github.com/SyamPrasadThota/Health_Assistant_Chatbot.git
cd Health_Assistant_Chatbot
````

2. **Create a virtual environment**:

```bash
python -m venv venv
venv\Scripts\activate      # For Windows
# OR
source venv/bin/activate   # For macOS/Linux
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```
4. **Install Dataset**:

Download the intents.json available in Kaggle

---

## 🚀 Usage

Run the chatbot application locally:

```bash
python app.py
```

Then open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 📁 Folder Structure

```
AI-Chatbot/
│
├── app.py                     
├── chat_model.h5              
├── intents.json               #You can downoad it from kaggle
├── label_encoder.pkl          
├── tokenizer.pkl            
│
├── templates/                 
│   └── index.html
```

---

## 💡 Technologies Used

* Flask (Python Web Framework)
* TensorFlow/Keras (Deep Learning)
* scikit-learn (Encoding/Preprocessing)
* HTML (Frontend)
* JSON (Intent definitions)

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch

```bash
git checkout -b feature/AmazingFeature
```

3. Commit your changes

```bash
git commit -m "Add some AmazingFeature"
```

4. Push to your branch

```bash
git push origin feature/AmazingFeature
```

5. Open a Pull Request

