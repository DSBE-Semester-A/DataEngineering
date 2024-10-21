import json
import os

import pandas as pd
from flask import jsonify
import pickle
import logging
from io import StringIO


class HairlossPredictor:
    def __init__(self, model_file):
        self.model = self.load_model(model_file)

    def load_model(self, model_file):
        # Load the model from the pickle file
        with open(model_file, 'rb') as f:
            model = pickle.load(f)
        return model

    def predict_single_record(self, prediction_input):
        logging.debug(prediction_input)
        if self.model is None:
            try:
                model_repo = os.environ['MODEL_REPO']
                file_path = os.path.join(model_repo, "hair_loss_model.pkl")
                with open(file_path, 'rb') as f:
                    self.model = pickle.load(f)
            except KeyError:
                print("MODEL_REPO is undefined")
                with open("hair_loss_model.pkl", 'rb') as f:
                    self.model = pickle.load(f)

        # Convert the JSON input into a DataFrame
        df = pd.DataFrame([prediction_input])
        #df = pd.read_json(StringIO(json.dumps(prediction_input)), orient='records')

        # Preprocessing the input data
        columns = ['Genetics', 'Environmental Factors', 'Smoking', 'Weight Loss', 'Poor Hair Care Habits', 'Hormonal Changes']
        for column in columns:
            df[column] = df[column].map({'Yes': 1, 'No': 0})

        df['Stress'] = df['Stress'].map({'High': 1.0, 'Moderate': 0.5, 'Low': 0.0})

        columns_to_encode = ['Medical Conditions', 'Medications & Treatments', 'Nutritional Deficiencies']
        for column in columns_to_encode:
            frequency_map = df[column].value_counts(normalize=True)
            df[column] = df[column].map(frequency_map)
        
        # Print the DataFrame to the console
        print("DataFrame used for prediction:\n", df)

        # Predict using the preprocessed data
        y_pred = self.model.predict(df)
        logging.info(y_pred[0])
        status = (y_pred[0] > 0.5)
        logging.info(type(status))
        #logging.info(type(status[0]))
        # return the prediction outcome as a json message. 200 is HTTP status code 200, indicating successful completion
        return jsonify({'result': str(status[0])}), 200
