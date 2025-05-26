from flask import Flask, render_template, request
from statistics import mode
import pickle

import numpy as np

app = Flask(__name__)

with open('modeldt.pkl', 'rb') as file:
    modeldt = pickle.load(file)

# Define the home page
@app.route('/')
def home():
    return render_template('home.html')

#Define a route for the form page
@app.route('/form')
def form():
    return render_template('form.html')

# Define the prediction page
@app.route('/submit', methods=['POST'])
def submit():
    # Get the form data from the request
    online_order = int(request.form['online_order'])
    booking = int(request.form['booking'])
    votes = int(request.form['votes'])
    location = int(request.form['location'])
    rest_type = int(request.form['rest_type'])
    cost = int(request.form['cost'])
    types = int(request.form['types'])

    prediction = modeldt.predict([[online_order, booking, votes, location, rest_type, cost, types]])

    # Return the prediction to the user
    if prediction == 1:
        return render_template('good.html')
    else:
        return render_template('bad.html')

if __name__ == '__main__':
    app.run(debug=True)