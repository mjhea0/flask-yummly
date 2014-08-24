from flask import render_template
from flask import request

from yummly import app
from database import session
import api
from models import Recipe 
import json


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", recipes=[])

@app.route("/", methods=["POST"])
def recipes():
    print "Calling get ingredients"
    ingredient = request.form["exampleInputIngredient"]
    response = api.get_ingredients(str(ingredient))
    search_response = json.loads(response)
    recipes = []
    matches = search_response.get("matches")
    for match in matches:
        recipe = Recipe(name=match.get("recipeName"),
            ingredients=match.get("ingredients"))
        recipes.append(recipe)
        print match.get("id"), match.get("recipeName"), match.get("ingredients")
    return render_template("index.html", recipes=recipes)