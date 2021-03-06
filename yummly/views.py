import random
import requests

import requests_cache

requests_cache.install_cache('demo_cache')

from flask import render_template, request, jsonify, \
    session, flash, redirect, url_for
from flask.ext.login import current_user, login_required, \
    login_user, logout_user

from twilio.rest import TwilioRestClient

from yummly import app, bcrypt, db, api
from yummly.forms import LoginForm, AddUserForm
from models import User, Recipe

from secret import sid, token


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(
                user.password, request.form['password']):
            session['logged_in'] = True
            login_user(user)
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@app.route('/new_user', methods=['GET', 'POST'])
def adduser():
    error = None
    form = AddUserForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if user or email:
            error = "User already exists. Please try again"
        else:
            user = User(username=form.username.data, email=form.email.data,
                        password=form.password.data)
            db.session.add(user)
            db.session.commit()
            session['logged_in'] = True
            return redirect(url_for('index'))

    return render_template('new_user.html', form=form, error=error)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('login'))


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """
    1. grab ingredient list from form
    2. pass ingredients list to `get_ingredients()`
    3. grab random result
    3. return results to the template
    """

    if request.method == "POST":
        ingredient_list = request.form.get('ingredient_list')
        recipe = []

        try:  # REFACTOR TRY/EXCEPT
            response = api.get_ingredients(ingredient_list)
            recipe = random.choice(response["matches"])
            print response
            ingredients = []
            for i in recipe['ingredients']:
                ingredients.append(i)

            try:
                image = recipe['imageUrlsBySize']['90'].replace(
                    's90-c', 's230-c')
            except:
                image = 'https://static.apitools.com/logos/yummly.png'

            result = {
                "recipe_id": recipe["id"],
                "recipe_name": recipe["recipeName"],
                "recipe_pic": image,
                "recipe_rating": recipe['rating'],
                "recipe_ingredients": ingredients
            }
            code = 200
        except requests.ConnectionError:
            result = {"sorry": "Sorry, your connection isn't working! Fix it!"}
            code = 500
        except:
            result = {"sorry": "Sorry, no results! Please try again."}
            code = 500
        print result
        return jsonify(result), code

    else:
        return render_template("index.html")


@app.route("/api/v1/recipes", methods=["GET", "POST"])
@login_required
def recipe_collection():
    """
    1. grab recipes from database
    2. pass recipes to list
    3. return results to the template
    """
    if request.method == "GET":
        all_recipes = db.session.query(Recipe).filter_by(
            user_id=current_user.get_id())
        recipes = []

        for recipe in all_recipes:
            result = {
                "recipe_id": recipe.id,
                "title": recipe.title,
                "url": recipe.url,
                "user_id": recipe.user_id,
                "recipe_pic": recipe.pic,
                "ingredients": recipe.ingredients,
                "yummly_id": recipe.yummly_id
            }
            recipes.append(result)
            result = recipes
            code = 200
        return jsonify(result=recipes), code

    if request.method == "POST":
        try:
            recipe_title = request.form.get('recipe_title')
            recipe_url = request.form.get('recipe_url')
            user = current_user.get_id()
            recipe_pic = request.form.get('recipe_pic')
            recipe_ingredients = request.form.get('recipe_ingredients')
            yummly_id = request.form.get('yummly_id')
            recipe = Recipe(
                title=recipe_title,
                url=recipe_url,
                user_id=user,
                pic=recipe_pic,
                ingredients=recipe_ingredients,
                yummly_id=yummly_id
            )
            db.session.add(Recipe(
                recipe_title, recipe_url, user,
                recipe_pic, recipe_ingredients, yummly_id)
            )
            db.session.commit()
            return jsonify({"Success": "Recipe added."}), 200
        except:
            return jsonify({"Error": "Recipe not saved."}), 500


@app.route("/recipes", methods=["GET", "POST"])
@login_required
def saved_recipes():
    return render_template("recipes.html")


@app.route("/recipe/<int:recipe_id>")
@login_required
def ingredients_list(recipe_id):
    error = ""
    single_recipe = db.session.query(Recipe).filter_by(id=recipe_id).first()
    try:
        response = api.get_ingredient_list(single_recipe.yummly_id)
        ingredients = response["ingredientLines"]

    except:
        error = "No ingredients found."

    return render_template(
        "single_recipe.html",
        ingredients=ingredients,
        id=recipe_id,
        error=error)


@app.route("/recipe/<int:recipe_id>/sms", methods=["GET", "POST"])
@login_required
def send_sms(recipe_id):
    error = ""
    number = "+1" + request.form.get('phone_number')
    single_recipe = db.session.query(Recipe).filter_by(id=recipe_id).first()
    try:
        response = api.get_ingredient_list(single_recipe.yummly_id)
        ingredients = response["ingredientLines"]
        name = response["name"]

        shopping_list = '\n'.join(ingredients)
        sms = name + " ingredients: " + shopping_list
        print sms
        print number

        account_sid = sid
        auth_token = token
        client = TwilioRestClient(account_sid, auth_token)
        client.messages.create(to=number, from_="+19419607434", body=sms)
        return sms
    except:
        error = "No ingredients found."
        return error


@app.route("/api/v1/recipes/<int:recipe_id>", methods=["GET", "POST"])
def recipe_element(recipe_id):
    if request.method == "GET":
        single_recipe = db.session.query(Recipe).filter_by(id=recipe_id).first()
        if single_recipe:
            result = {
                "recipe_id": single_recipe.id,
                "title": single_recipe.title,
                "url": single_recipe.url,
                "user_id": single_recipe.user_id,
                "user_id": single_recipe.user_id,
                "recipe_pic": single_recipe.pic,
                "ingredients": single_recipe.ingredients
            }
            return jsonify(result)
        else:
            return jsonify({"Error": "Recipe does not exist."}), 404

    if request.method == "POST":
        try:
            db.session.query(Recipe).filter_by(id=recipe_id).delete()
            db.session.commit()
            return jsonify({"Success": "Recipe deleted."}), 200
        except:
            return jsonify({"Error": "Recipe does not exist."}), 500
