# API for real estate price estimation based on a linear regression model

This repository contains the code of a webservice that provides an api for predicting the price of a property based on several characteristics.

The app is deployed on heroku and can be accessed via https://immo-eliza-ql.herokuapp.com/

# Requirements

This app runs on python 3.8. For other rrequirements, see the file `requirements.txt`.

# Instruction

To run the app, just issue the following command in a terminal:

```bash

python app.py
```

The app has three routes: `/`, `/predict` and `/predict/format`. The route `/` allows only a GET request, which returns a welcome message if the server is running or an error otherwise. The route `/predict` allows GET and POST requests. The GET request returns a message that explains how to issue a POST request (see the following paragraph for more details) and the POST request, given data about a property (in JSON format), returns a prediction of the price of the property or an error if the data sent is not in the appropriate format, each response being sent in JSON format. 

As mentionned above, predictions are obtained using a POST request at the route `/predict` by sending data in JSON format using a prescribed schema, which can be found as a result of a GET request at `/predict/format`.
```json
 {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "description": "Format required for the property's data.",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "Livable surface": {"type": "number", "minimum": 0},
                "Type of property": {
                    "type": "string",
                    "enum": ["flat", "house"],
                },
                "Number of bedrooms": {"type": "integer", "minimum": 0},
                "Balcony": {"type": "boolean"},
                "Garage": {"type": "boolean"},
                "Surface bedroom 1": {"type": "number", "minimum": 0},
                "Surface garden": {"type": "number", "minimum": 0},
                "Garden": {"type": "boolean"},
                "Surface kitchen": {"type": "number", "minimum": 0},
                "Cellar": {"type": "boolean"},
                "Surface of living-room": {"type": "number", "minimum": 0},
                "Furnished": {"type": "boolean"},
                "Kitchen equipment": {
                    "type": "string",
                    "enum": [
                        "NOT EQUIPPED",
                        "PARTIALLY EQUIPPED",
                        "SUPER EQUIPPED",
                        "FULLY EQUIPPED",
                    ],
                },
                "Terrace": {"type": "boolean"},
                "Surface terrace": {"type": "number", "minimum": 0},
                "Number of facades": {"type": "integer", "minimum": 0},
                "State of the property": {
                    "type": "string",
                    "enum": [
                        "EXCELLENT",
                        "NORMAL",
                        "TO BE RENOVATED",
                        "RENOVATED",
                        "NEW",
                    ],
                },
            },
            "required": [
                "Livable surface",
                "Type of property",
                "Number of bedrooms",
            ],
        }
    },
    "required": ["data"],
}

```
