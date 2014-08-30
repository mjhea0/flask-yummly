from flask import render_template, request

from yummly import app
import api 
import json


@app.route("/", methods=["GET", "POST"])
def index():
    recipe_response = []
    ingredients = []

    if request.method == "POST":
        print "Calling get ingredients"
        ingredient = request.form["exampleInputIngredient"]
        response = api.get_ingredients(ingredient) # api call
        search_response = json.loads(response)

        matches = search_response["matches"]
        for match in matches:
            recipe_response.extend([
                match["recipeName"], match["smallImageUrls"][0], match["id"]])
            ingredients.append(match["ingredients"])
            break # just one result
        ingredients = ingredients[0]

    """    
    match_image = search_response["matches"][0]["smallImageUrls"][0]
    match_id = search_response["matches"][0]["id"]
    match_url = "http://www.yummly.com/recipe/{0}".format(match_id)
    recipe_response.extend([match_name, match_image])
    
    ingredient_response = search_response["matches"][0]["ingredients"]
    ingredients = json.dumps(ingredient_response)
    """

    return render_template(
        "index.html", 
        recipe_response=recipe_response, 
        ingredients=ingredients)
