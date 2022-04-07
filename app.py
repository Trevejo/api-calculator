from ast import If
from datetime import datetime

import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

results = []

@app.route("/", methods=["GET"])
def home():
    return "Welcome to Api Calculator!"

@app.route("/results", methods=["GET"])
def resultsHistory():
  return jsonify(results)

@app.route("/operate", methods=["GET"])
def operate():
    if "operation" in request.args:
        operation = request.args["operation"]
    else:
       return dict(error="Calculation Error", message="Invalid operation")
    result = 0
    try:
        if "+" in operation:
            operatee = operation.split("+")
            result = int(operatee[0]) + int(operatee[1])
        if "-" in operation:
            operatee = operation.split("-")
            result = int(operatee[0]) - int(operatee[1])
        if "*" in operation:
            operatee = operation.split("*")
            result = int(operatee[0]) * int(operatee[1])
        if "/" in operation:
            operatee = operation.split("/")
            result = int(operatee[0]) / int(operatee[1])
        response = {"updated_date": datetime.now(), "operation": operation, "result": result}
        results.append(response)
        return response
    except Exception as e:
        return dict(error="Calculation Error", exception=str(e), message="Review operation parameters and try again")

if __name__ == "__main__":
    app.run(host="0.0.0.0")