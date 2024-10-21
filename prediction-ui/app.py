# importing Flask and other modules
import json
import os
import logging
import requests
from flask import Flask, request, render_template, jsonify
import pickle

# Flask constructor
app = Flask(__name__)

# which URL is associated function
@app.route('/checkhairloss', methods=["GET", "POST"])
def check_hairloss():
    if request.method == "GET":
        return render_template("input_form_page.html")

    elif request.method == "POST":
        prediction_input = [
            {
            "Genetics": request.form.get("history"),
            "Hormonal Changes": request.form.get("hormonal"),
            "Medical Conditions": request.form.get("medical"),
            "Medications & Treatments": request.form.get("medications"),
            "Nutritional Deficiencies": request.form.get("nutritional"),
            "Stress": request.form.get("stress"),
            "Age": int(request.form.get("age", 0)),
            "Poor Hair Care Habits": request.form.get("hair_care"),
            "Environmental Factors": request.form.get("environment"),
            "Smoking": request.form.get("smoke"),
            "Weight Loss": request.form.get("weightloss")
            }
        ]

        # Print raw input data to the console
        print("Form input received: ", prediction_input)

        logging.debug("Prediction input : %s", prediction_input)

        # use requests library to execute the prediction service API by sending an HTTP POST request
        # use an environment variable to find the value of the diabetes prediction API
        # json.dumps() function will convert a subset of Python objects into a json string.
        # json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.
        predictor_api_url = os.environ.get('PREDICTOR_API', 'http://35.222.44.63:5001')
        res = requests.post(predictor_api_url, json=json.loads(json.dumps(prediction_input)))

        # Make prediction using the loaded model
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
