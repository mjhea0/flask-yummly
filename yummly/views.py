from flask import render_template, request

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
        
        ingredient_list = request.form['ingredient']  
        single_recipe = []

        try:
            response = api.get_ingredients(ingredient_list) 
            single_recipe = random.choice(response["matches"])


        except: # silencing all errors
            #if not single_recipe:
            errors.append("No results! Try again.")

        return render_template(
            "index.html", 
            recipe=single_recipe,
            recipes=response,
            errors=errors)

    else:

        return render_template("index.html")

