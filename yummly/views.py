from flask import render_template
from flask import request

from yummly import app
import api 
import json
from flask import jsonify


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", recipes=[])
"""
@app.route("/", methods=["POST"])
def recipes():
    print "Calling get ingredients"
    ingredient = request.form["exampleInputIngredient"]
    response = api.get_ingredients(str(ingredient))
    search_response = json.loads(response)
    # return jsonify[search_response]
    recipes = []
    matches = search_response.get("matches")
    for match in matches:
        recipe = Recipe(name=match.get("recipeName"),
            ingredients=json.dumps(match.get("ingredients")),
            image=json.dumps(match.get("smallImageUrls")))
        recipes.append(recipe)
    print type(recipes)
    #    print json.dumps(match.get("ingredients"))
    return render_template("index.html", recipes=recipes)
    # return jsonify(test)
"""
@app.route("/", methods=["POST"])
def recipes():
    print "Calling get ingredients"
    ingredient = request.form["exampleInputIngredient"]
    response = api.get_ingredients(str(ingredient))
    search_response = json.loads(response)
    recipe_response = []
    ingredients = []
    match_name = search_response["matches"][0]["recipeName"]
    match_image = search_response["matches"][0]["smallImageUrls"][0]
    match_id = search_response["matches"][0]["id"]
    match_url = "http://www.yummly.com/recipe/{0}".format(match_id)
    recipe_response.extend([match_name, match_image])

    ingredient_response = search_response["matches"][0]["ingredients"]
    ingredients = json.dumps(ingredient_response)
    print ingredients
    print match_url
    return render_template("index.html", match_name=match_name, match_image=match_image, ingredients=ingredients, match_url=match_url)
    #   return jsonify(matches)

# add separate Get Recipe API call to obtain the URL that matches each recipe ID 
