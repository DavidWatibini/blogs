import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')

    BASE_URL = 'http://quotes.stormconsultancy.co.uk/{}.json'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:wati@localhost/blogs'


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
