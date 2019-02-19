import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')

    BASE_URL = 'http://quotes.stormconsultancy.co.uk/{}.json'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:wati@localhost/blog'


class ProdConfig(Config):

	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
