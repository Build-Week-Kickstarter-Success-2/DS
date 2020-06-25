
from flask import Blueprint, render_template

#+1
# Dependencies
from flask import Flask, request, jsonify, Blueprint
import os
import pickle
# import joblib #TODO: retire this
import traceback
import pandas as pd
import numpy as np
import category_encoders

def load_model():
    print("LOADING THE MODEL...")
    with open(MODEL_FILEPATH, "rb") as model_file:
        saved_model = pickle.load(model_file)
    return saved_model

#+2
MODEL_FILEPATH = os.path.join(os.path.dirname(__file__),"..","..", "model", "model (3).p")
# MODEL_FILEPATH = '/Users/jasimrashid/Projects/DS/model/model (3).p'
lr = load_model()



home_routes = Blueprint("home_routes", __name__)
# stats_routes = Blueprint("stats_routes", __name__) #-5

@home_routes.route("/")
def index():
    return render_template("prediction_form.html")



@home_routes.route('/predict', methods=['POST'])
def predict_json():
    if lr:
        try:
            json_ = request.json
            print(json_)            
            query = pd.DataFrame(json_)
            prediction = list(lr.predict(query))
            prediction_proba = list(lr.predict_proba(query))

            return jsonify(prediction = str(prediction), prediction_proba=prediction_proba[0][1])

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')





#ROUTE FOR RUNNING APP THROUGH BROWSWER REQUEST TODO: UPDATE THIS AFTER MVP
@home_routes.route("/predict_form", methods=["POST"])
def predict_html():
    category = request.form["category"]
    pitch = request.form["pitch"]
    a_ = int(request.form["a"])
    b_ = int(request.form["b"])
    #FOR TESTING PURPOSES ONLY - THE MODEL ONLY USES X AND Y FROM THE FORM
    # clf = load_model()
    # print("CLASSIFIER:", clf)
    # inputs = [[a_, b_]]
    # print(type(inputs), inputs)
    # result = clf.predict(inputs)
    # print("RESULT:", result)
    # print("-----------------")
    # print("*********** MAKING A PREDICTION...")
    
    # breakpoint()

    return jsonify({
       "message": "successful"

    })



