from flask import Flask, request, jsonify
import predict.prediction as p
import os
import preprocessing.cleaning as c
import jsonschema
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "I'm alive!"

schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "description": "Format required for the property's data.",
    "properties": {"data": {
        "type": "object",
        "properties": {
            "Livable surface": {
                "type": "number",
                "minimum": 0
            },
            "Type of property": {
                "type": "string",
                "enum": ["flat", "house"]
            },
            "Number of bedrooms": {
                "type": "integer",
                "minimum": 0
            },
            "Balcony": {
                "type": "boolean"
            },
            "Garage": {
                "type": "boolean"
            },
            "Surface bedroom 1": {
                "type": "number",
                "minimum": 0
            },
            "Surface garden": {
                "type": "number",
                "minimum": 0
            },
            "Garden": {
                "type": "boolean"
            },
            "Surface kitchen": {
                "type": "number",
                "minimum": 0
            },
            "Cellar": {
                "type": "boolean"
            },
            "Surface of living-room": {
                "type": "number",
                "minimum": 0
            },
            "Furnished": {
                "type": "boolean"
            },
            "Kitchen equipment": {
                "type": "string",
                "enum": ["NOT EQUIPPED", "PARTIALLY EQUIPPED", "SUPER EQUIPPED", "FULLY EQUIPPED"]
            },
            "Terrace": {
                "type": "boolean"
            },
            "Surface terrace": {
                "type": "number",
                "minimum": 0
            },
            "Number of facades": {
                "type": "integer",
                "minimum": 0
            },
            "State of the property": {
                "type": "string",
                "enum": ["EXCELLENT", "NORMAL", "TO BE RENOVATED", "RENOVATED", "NEW"]
            }
        },
        "required": ["Livable surface", "Type of property", "Number of bedrooms"]
    }
                   },
    "required": ["data"]
}


@app.route("/predict", methods=['POST', 'GET'])
def predict():
    if request.method == "GET":
        message = (
            " Hi!\n In order to obtain a prediction of the price of "
            "your property, please supply the data in json format as "
            "described in /predict/format."
            )
        return message
    if request.method == 'POST':
        json0 = request.get_json()
        try:
            v = jsonschema.Draft3Validator(schema)
            v.validate(json0)
            json = json0["data"]
            c.cleaning(json)
            c.one_hot(json)
            data = c.data_to_array(json)
            return jsonify(price = p.predict(data, "./model/model.joblib"))
        except jsonschema.exceptions.ValidationError as err:
            errors = sorted(v.iter_errors(json0), key=lambda e: e.path)
            return jsonify(errors=[error.message for error in errors])


@app.route("/predict/format", methods=["GET"])
def format():
    return jsonify(schema)
if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)
