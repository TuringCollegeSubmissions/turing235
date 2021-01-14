from flask import Flask, request
import numpy as np
import pickle
import json

SAVED_MODEL_PATH = "classifier.pkl"
clf = pickle.load(open(SAVED_MODEL_PATH, "rb"))

app = Flask(__name__)


def __process_input(request_data: str) -> np.array:
    """
    Converts input request data into numpy array
    :param request_data in json format
    :return: numpy array
    """
    return np.asarray(json.loads(request_data)["input"])


@app.route("/")
def what_is_up():
    """Initial message"""
    return 'Turing235 Project'


@app.route("/predict", methods=["POST"])
def predict() -> str:
    """
    Prediction function
    :param: None
    :return: Predicted values in json format. In case of error return error message and 400
    """
    input_params = __process_input(request.data)
    try:
        prediction = clf.predict(input_params)
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 400
    return json.dumps({"Predicted values": prediction.tolist()})


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
