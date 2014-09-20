from flask import render_template, request, jsonify

from yummly import app
from yummly import api 
import random


@app.route("/", methods=["GET", "POST"])
def index():
    """
    1. grab ingredient list from form
    2. pass ingredients list to `get_ingredients()`
    3. grab random result
    3. return results to the template
    """

    if request.method == "POST":
        errors = [] 
        result = []
        ingredient_list = request.form.get('ingredient_list') 

        try:
            response = api.get_ingredients(ingredient_list) 
            single_recipe = random.choice(response["matches"])
            result = {
                "recipe_id": single_recipe["id"],
                "recipe_name": single_recipe["recipeName"],
                "recipe_pic": single_recipe['imageUrlsBySize']['90'].replace(
                    's90-c', 's230-c')
            }
            code = 200

        except: # silencing all errors
            result = {"sorry": "Sorry, no results! Please try again."}
            code = 404


        return jsonify(result)

    else:

        return render_template("index.html")

