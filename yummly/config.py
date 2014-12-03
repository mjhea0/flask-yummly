class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = "not-a-good-secret"


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///yummly_test.db"


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "update"
    DEBUG = False
