class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = "not-a-good-secret"


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///yummly_test.db"


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "postgres://zgaejodwfynffw:cF8w21iRoZ9cpKfmwvFFisksk_@ec2-54-83-199-115.compute-1.amazonaws.com:5432/dairfoj5de3au0"
    DEBUG = False