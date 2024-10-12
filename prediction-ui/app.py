# importing Flask and other modules
import json
import os
import logging
import requests
from flask import Flask, request, render_template, jsonify

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/checkhairloss', methods=["GET", "POST"])
def check_diabetes():
    if request.method == "GET":
        return render_template("input_form_page.html")

    elif request.method == "POST":
        prediction_input = [
            {
            "history": 1 if request.form.get("history") == "Yes" else 0,
            "hormonal": 1 if request.form.get("hormonal") == "Yes" else 0,
            "medical": request.form.get("medical"),
            "medication": request.form.get("medication"),
            "nutritional": request.form.get("nutritional"),
            "stress": 0 if request.form.get("stress") == "Low" else 1 if request.form.get("stress") == "Moderate" else 2,
            "age": 1 if request.form.get("age") == "Yes" else 0,
            "hair_care": 1 if request.form.get("hair_care") == "Yes" else 0,
            "environment": 1 if request.form.get("environment") == "Yes" else 0,
            "smoke": 1 if request.form.get("smoke") == "Yes" else 0,
            "weightloss": 1 if request.form.get("weightloss") == "Yes" else 0
            }
        ]

        logging.debug("Prediction input : %s", prediction_input)

        # use requests library to execute the prediction service API by sending an HTTP POST request
        # use an environment variable to find the value of the diabetes prediction API
        # json.dumps() function will convert a subset of Python objects into a json string.
        # json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.
        predictor_api_url = os.environ['PREDICTOR_API']
        res = requests.post(predictor_api_url, json=json.loads(json.dumps(prediction_input)))

        prediction_value = res.json()['result']
        logging.info("Prediction Output : %s", prediction_value)
        return render_template("response_page.html",
                               prediction_variable=prediction_value)

    else:
        return jsonify(message="Method Not Allowed"), 405  # The 405 Method Not Allowed should be used to indicate
    # that our app that does not allow the users to perform any other HTTP method (e.g., PUT and  DELETE) for
    # '/checkdiabetes' path


# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)
