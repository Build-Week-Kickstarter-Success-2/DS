
from flask import Blueprint, render_template
from flask import Flask, request, jsonify, Blueprint
import os
import pickle
import traceback
import pandas as pd
import numpy as np
import category_encoders

def load_model():
    print("LOADING THE MODEL...")
    with open(MODEL_FILEPATH, "rb") as model_file:
        saved_model = pickle.load(model_file)
    return saved_model

# Specify the filepath
MODEL_FILEPATH = os.path.join(os.path.dirname(__file__),"..","..", "model", "model (3).p")
lr = load_model()

home_routes = Blueprint("home_routes", __name__)

# Web app home route
@home_routes.route("/")
def index():
    categories = ['3D Printing', 'Academic', 'Accessories', 'Action', 'Animals', 'Animation', 'Anthologies', 'Apparel', 'Apps', 'Architecture', 'Art', 'Art Books', 'Audio', 'Bacon', 'Blues', 'Calendars', 'Camera Equipment', 'Candles', 'Ceramics', "Children's Books", 'Childrenswear', 'Chiptune', 'Civic Design', 'Classical Music', 'Comedy', 'Comic Books', 'Comics', 'Community Gardens', 'Conceptual Art', 'Cookbooks', 'Country & Folk', 'Couture', 'Crafts', 'Crochet', 'DIY', 'DIY Electronics', 'Dance', 'Digital Art', 'Documentary', 'Drama', 'Drinks', 'Electronic Music', 'Embroidery', 'Events', 'Experimental', 'Fabrication Tools', 'Faith', 'Family', 'Fantasy', "Farmer's Markets", 'Farms', 'Fashion', 'Festivals', 'Fiction', 'Film & Video', 'Fine Art', 'Flight', 'Food', 'Food Trucks', 'Footwear', 'Gadgets', 'Games', 'Gaming Hardware', 'Glass', 'Graphic Design', 'Graphic Novels', 'Hardware', 'Hip-Hop', 'Horror', 'Illustration', 'Immersive', 'Indie Rock', 'Installations', 'Interactive Design', 'Jazz', 'Jewelry', 'Journalism', 'Kids', 'Knitting', 'Latin', 'Letterpress', 'Literary Journals', 'Literary Spaces', 'Live Games', 'Makerspaces', 'Metal', 'Mixed Media', 'Mobile Games', 'Movie Theaters', 'Music', 'Music Videos', 'Musical', 'Narrative Film', 'Nature', 'Nonfiction', 'Painting', 'People', 'Performance Art', 'Performances', 'Periodicals', 'Pet Fashion', 'Photo', 'Photobooks', 'Photography', 'Places', 'Playing Cards', 'Plays', 'Poetry', 'Pop', 'Pottery', 'Print', 'Printing', 'Product Design', 'Public Art', 'Publishing', 'Punk', 'Puzzles', 'Quilts', 'R&B', 'Radio & Podcasts', 'Ready-to-wear', 'Residencies', 'Restaurants', 'Robots', 'Rock', 'Romance', 'Science Fiction', 'Sculpture', 'Shorts', 'Small Batch', 'Social Practice', 'Software', 'Sound', 'Space Exploration', 'Spaces', 'Stationery', 'Tabletop Games', 'Taxidermy', 'Technology', 'Television', 'Textiles', 'Theater', 'Thrillers', 'Toys', 'Translations', 'Typography', 'Vegan', 'Video', 'Video Art', 'Video Games', 'Wearables', 'Weaving', 'Web', 'Webcomics', 'Webseries', 'Woodworking', 'Workshops', 'World Music', 'Young Adult', 'Zines']
    return render_template("prediction_form.html", categories=categories)

# Predict route - called via API 
@home_routes.route('/predict', methods=['POST'])
def predict_json():
    if lr:
        try:
            json_ = request.json
            print(json_)            
            query = pd.DataFrame(json_)
            query_dict = query.to_dict()
            prediction = list(lr.predict(query))
            prediction_proba = list(lr.predict_proba(query))
            # breakpoint()
            #TODO: set correct datatypes and validate datatypes
            return jsonify(features = query_dict, prediction = str(prediction), prediction_proba=prediction_proba[0][1])
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

# Predict route - called via web-app
@home_routes.route("/predict_form", methods=["POST"])
def predict_html():
    category = request.form["category"]
    staff_pick = 1 if request.form["staff_pick"] == "True" else 0
    staff_pick = bool(staff_pick)
    description_leng = int(request.form["description_leng"])
    usd_goal = int(request.form["usd_goal"])
    cam_length = int(request.form["cam_length"])
    column_names = ["category","staff_pick","description_leng","usd_goal","cam_length"]
    df_row = pd.DataFrame(columns = column_names)
    # df_row.append([[category,staff_pick,description_leng,usd_goal,cam_length]])
    df_row = df_row.append({'category':category,'staff_pick':staff_pick,'description_leng':description_leng,'usd_goal':usd_goal,'cam_length': cam_length},ignore_index=True)
    df_row_dict = df_row.to_dict()
    #TODO: form design slider shows values for
    prediction = list(lr.predict(df_row))
    prediction_proba = list(lr.predict_proba(df_row))
    prediction_text = "Success" if prediction[0] == 1 else "Fail"
    print(jsonify(prediction = str(prediction), prediction_proba=prediction_proba[0][1]))
    # return jsonify(features = df_row_dict, prediction = str(prediction), prediction_proba=prediction_proba[0][1])
    return render_template("prediction_results.html", features = df_row_dict, prediction = str(prediction_text), prediction_proba=prediction_proba[0][1])

    #TODO: exception handling like for predict_json
    # TODO: should this be consolidted with the predict_json route?



