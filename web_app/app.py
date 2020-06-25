# Dependencies
from flask import Flask, request, jsonify, Blueprint
import os
import pickle
# import joblib #TODO: retire this
import traceback
import pandas as pd
import numpy as np
import category_encoders



# TODO: congigure os path for models
MODEL_FILEPATH = os.path.join(os.path.dirname(__file__),"..", "model", "model (3).p")

# stats_routes = Blueprint("stats_routes", __name__) #-3
# Your API definition
# app = Flask(__name__) #-4

stats_routes = Blueprint("stats_routes", __name__)

# ROUTE TO CALL PREDICTION FROM API
@app.route('/predict', methods=['POST'])
def predict_json():
    if lr:
        try:
            json_ = request.json
            print(json_)
            
            # OPTION A
            # query = pd.get_dummies(pd.DataFrame(json_))
            # query = query.reindex(columns=model_columns, fill_value=0)
            # breakpoint()
            #OPTION B
            query = pd.DataFrame(json_)
            # query = query[['a','b']]

            prediction = list(lr.predict(query))
            prediction_proba = list(lr.predict_proba(query))

            # return jsonify({'prediction': str(prediction)})
            return jsonify(prediction = str(prediction), prediction_proba=prediction_proba[0][1])

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')



# TRAIN AND SAVE MODEL AS A SERIALIZABLE FILE
# def train_and_save_model():
#     print("TRAINING THE MODEL...")
#     X, y = load_iris(return_X_y=True)
#     classifier = LogisticRegression() # for example
#     classifier.fit(X, y)

#     print("SAVING THE MODEL...")
#     with open(MODEL_FILEPATH, "wb") as model_file:
#         pickle.dump(classifier, model_file)
#     return classifier

# LOAD SERIALIZED MODEL
def load_model():
    print("LOADING THE MODEL...")
    with open(MODEL_FILEPATH, "rb") as model_file:
        saved_model = pickle.load(model_file)
    return saved_model


# ROUTE FOR RUNNING APP THROUGH BROWSWER REQUEST TODO: UPDATE THIS AFTER MVP
@stats_routes.route("/predict_form", methods=["POST"])
def predict_html():
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form)) #> {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}
    # breakpoint()
    category = request.form["category"]
    pitch = request.form["pitch"]
    a_ = int(request.form["a"])
    b_ = int(request.form["b"])


    #FOR TESTING PURPOSES ONLY - THE MODEL ONLY USES X AND Y FROM THE FORM
    clf = load_model()
    print("CLASSIFIER:", clf)
    inputs = [[a_, b_]]
    print(type(inputs), inputs)
    result = clf.predict(inputs)
    print("RESULT:", result)
    print("-----------------")
    print("*********** MAKING A PREDICTION...")
    
    # breakpoint()

    return jsonify({
       "message": "BOOK CREATED OK",
       "all features": dict(request.form),
       "feature used by model a": a_,
       "feature used by model b": b_,
       "predicted outcome: ": int(result[0])

    })


# MAIN
if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    # LOAD MODEL - OPTION A
    # lr = joblib.load("model_test.pkl") # Load "model.pkl"

    # LOAD MODEL - OPTION B
    lr = load_model()
    print("CLASSIFIER:", lr)

    print ('Model loaded')
    # model_columns = joblib.load("model_test_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')

    app.run(port=port, debug=True)