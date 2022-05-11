import flask
from flask import json, request, render_template

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    #json testing
    data_set = {'Page': 'Home', 'Message': 'Welcome to api calculator homepage!'}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route("/operate", methods=["GET"])
def operate():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")