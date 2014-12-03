import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

print os.environ['APP_SETTINGS']

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

import api
import views

from models import User
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
