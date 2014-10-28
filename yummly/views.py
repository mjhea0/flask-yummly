from flask import render_template, request, jsonify, \
    session, flash, redirect, url_for

from yummly import app, bcrypt, db
from yummly import api
import random
import requests

from functools import wraps
from yummly.forms import LoginForm, AddUserForm
from models import User


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(
                user.password, request.form['password']):
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@app.route('/new_user', methods=['GET', 'POST'])
def adduser():
    error = None
    form = AddUserForm(request.form)
    if form.validate_on_submit():
        if form.password.data != form.password2.data:
            error = "Passwords must match!"
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
    session.pop('logged_in', None)
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

        try:
            response = api.get_ingredients(ingredient_list)
            recipe = random.choice(response["matches"])

            ingredients = []
            for i in recipe['ingredients']:
                ingredients.append(i)

            result = {
                "recipe_id": recipe["id"],
                "recipe_name": recipe["recipeName"],
                "recipe_pic": recipe['imageUrlsBySize']['90'].replace(
                    's90-c', 's230-c'),
                "recipe_rating": recipe['rating'],
                "recipe_flavors": recipe['flavors'],
                "recipe_ingredients": ingredients
            }
            code = 200
        except requests.ConnectionError:
            result = {"sorry": "Sorry, your connection isn't working! Fix it!"}
            code = 500
        except:
            result = {"sorry": "Sorry, no results! Please try again."}
            code = 500

        return jsonify(result), code

    else:
        return render_template("index.html")
