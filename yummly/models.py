from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from yummly import db, bcrypt


class Recipe(db.Model):

    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    pic = db.Column(db.String)
    ingredients = db.Column(db.String)
    yummly_id = db.Column(db.String)

    def __init__(self, title, url, user_id, pic, ingredients, yummly_id):
        self.title = title
        self.url = url
        self.user_id = user_id
        self.pic = pic
        self.ingredients = ingredients
        self.yummly_id = yummly_id

    def __repr__(self):
        return '< %r>' % self.title


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String)
    recipes = relationship("Recipe", backref="user")

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % self.username
