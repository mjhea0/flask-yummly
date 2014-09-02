from flask import render_template, request

from yummly import app
import api 
import json


@app.route("/", methods=["GET", "POST"])
def index():
    recipe_response = [] # this doesn't work if placed after "if request.method..."...??
    ingredients = []
    errors = []
    image = []
    if request.method == "POST":
        
        ingredient = request.form["exampleInputIngredient"]
        
        try:
            response = api.get_ingredients(ingredient) # api call
            search_response = json.loads(response)

            matches = search_response["matches"]
            for match in matches:

                image = match['imageUrlsBySize']['90'].replace('s90-c', 's230-c')
                
                recipe_response.extend([
                    match["recipeName"], image, match["id"]])
                ingredients.append(match["ingredients"])
                break # just one result for now
            ingredients = ingredients[0]
            print ingredients
            print recipe_response

        except: 
            errors.append("Something went wrong!")


    return render_template(
        "index.html", 
        recipe_response=recipe_response,
        ingredients=ingredients,
        errors=errors)

""" 
add search by cuisine?
Supported Cuisines:
American, Italian, Asian, Mexican, Southern & Soul Food, French, 
Southwestern, Barbecue, Indian, Chinese, Cajun & Creole, English, 
Mediterranean, Greek, Spanish, German, Thai, Moroccan, Irish, Japanese, 
Cuban, Hawaiin, Swedish, Hungarian, Portugese

include form for excluded ingredients
"""
