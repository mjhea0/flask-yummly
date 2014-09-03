from flask import render_template, request

from yummly import app
import api 
import json


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        errors = []

        ingredient = request.form["exampleInputIngredient"] # grabbing ingredient from form
        try:
            response = api.get_ingredients(ingredient) # api call
            #search_response = json.loads(response)

            #for match in response["matches"]: # loop through json results

                #image = match['imageUrlsBySize']['90'].replace('s90-c', 's230-c')
                
                #recipe_response.extend([match["recipeName"], image, match["id"]])
                #ingredients.append(match["ingredients"])
                #break # just one result for now
            #ingredients = ingredients[0]
            #print recipe_response

        except: 
            errors.append("Something went wrong!")


        return render_template(
            "index.html", 
            recipe_response=response,
            errors=errors)

    else:

        return render_template(
            "index.html"
        )
""" 
add search by cuisine?
Supported Cuisines:
American, Italian, Asian, Mexican, Southern & Soul Food, French, 
Southwestern, Barbecue, Indian, Chinese, Cajun & Creole, English, 
Mediterranean, Greek, Spanish, German, Thai, Moroccan, Irish, Japanese, 
Cuban, Hawaiin, Swedish, Hungarian, Portugese

include form for excluded ingredients
"""
