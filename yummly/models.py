from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base, engine

# models

class Recipe(Base):
    __tablename__ = "recipe"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    ingredients = Column(Text)
    image = Column(String)


class Ingredient(Base):
    __tablename__ = "ingredient"

    id = Column(Integer, primary_key=True)
    name = Column(Text)

