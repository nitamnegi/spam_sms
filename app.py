from flask import Flask, request, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)

# Load the model and feature extractor
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('feature_extraction.pkl', 'rb') as fe_file:
    feature_extraction = pickle.load(fe_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = feature_extraction.transform(data)
        prediction = model.predict(vect)
        result = "Spam" if prediction[0] == 0 else "Ham"
        return render_template('index.html', message=message, prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
