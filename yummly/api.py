# api calls


import requests
from secret import APP_ID, APP_KEY


def get_ingredients(ingredient_list):
    res = requests.get(
        "http://api.yummly.com/v1/api/recipes",
        params={
            '_app_id': APP_ID,
            '_app_key': APP_KEY,
            'q': ingredient_list,
            'maxResult': 100
        }
    )
    print res.from_cache
    return res.json()


def get_ingredient_list(recipe_id):
    res = requests.get(
        "http://api.yummly.com/v1/api/recipe/"+str(recipe_id),
        params={
            '_app_id': APP_ID,
            '_app_key': APP_KEY,
        }
    )
    return res.json()
