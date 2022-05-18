SERVER = "localhost"
DATABASE_USERNAME = "***"
DATABASE_PASSWORD = "***"

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DATABASE_USERNAME + ':' + DATABASE_PASSWORD + '@' + SERVER + ':3306/***'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class DeveplomentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False