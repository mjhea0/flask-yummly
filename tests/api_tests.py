# tests
import os
import unittest
from yummly import views, api
from urlparse import urlparse
import requests
import json
from secret import APP_ID, APP_KEY



class RecipeSearchTests(unittest.TestCase):
    def test_recipe_response(self):
        ingredient = "apples"
        response = requests.get(
        "http://api.yummly.com/v1/api/recipes",
        params={'_app_id': APP_ID, '_app_key': APP_KEY, 'q': ingredient}
        )
        print response.content

        self.assertEqual(urlparse(response.location).path, "/")
        self.assertEqual(response.mimetype, "application/json")
            

if __name__ == "__main__":
    unittest.main()






        