# Flask Yummly

Recipes -> Ingredients

[http://yummlyrecipe.herokuapp.com/](http://yummlyrecipe.herokuapp.com/)

## QuickStart

1. Clone
1. Create/Activate virtualenv
1. Set Environment variables - `export APP_SETTINGS="yummly.config.DevelopmentConfig"`
1. Create DB - `python create_db.py`
1. Run - python run.py

## Heroku Deploy

1. Create App / Push to Heroku
1. Add Database - `heroku addons:add heroku-postgresql`
1. Get Database URI - `heroku config | grep HEROKU_POSTGRESQL`
1. Add URI to `ProductionConfig` in *yummly/config.py* (i.e., - `SQLALCHEMY_DATABASE_URI = "foobar"`)
1. Set Environment variables = `heroku config:set APP_SETTINGS="yummly.config.ProductionConfig"`
1. Create DB - `heroku run python create_db.py`

Profit!!