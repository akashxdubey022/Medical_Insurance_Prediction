# app.py
from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load the ML model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        age = int(request.form['Age'])
        sex = int(request.form['Sex'])
        bmi = float(request.form['BMI'])
        children = int(request.form['Children'])
        smoker = int(request.form['Smoker'])
        region = int(request.form['Region'])

        # Make a prediction using the model
        prediction = model.predict([[age, sex, bmi, children ,smoker,region]])

        # Return the prediction as JSON
        return jsonify({'prediction': str(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
