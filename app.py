from flask import Flask, jsonify, request
from joblib import load

app = Flask(__name__)

@app.route('/')
def index():
    if 'query' not in request.args:
        return jsonify({"Prediction": None, "message":"Send me a text"})

    query = request.args.get('query')
    model = load('model.joblib')
    labels = ['carros', 'economia', 'educacao', 'esporte', 'musica', 'politica']

    predict = model.predict([query])
    prediction = labels[predict[0]]

    return jsonify({"prediction" : prediction})
