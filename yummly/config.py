class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = "not-a-good-secret"


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///yummly_test.db"


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "postgres://oedvvkohmyajhc:XV2GVjFLQm55SIb7VOuYCprAot@ec2-54-163-248-144.compute-1.amazonaws.com:5432/depat5j28d4ja3"
    DEBUG = False
