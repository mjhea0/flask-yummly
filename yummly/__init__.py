from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
config_path = os.environ.get("CONFIG_PATH", "yummly.config.Config")
app.config.from_object(config_path)
db = SQLAlchemy(app)

import api
import views
