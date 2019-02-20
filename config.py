import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')

    BASE_URL = 'http://quotes.stormconsultancy.co.uk/{}.json'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:wati@localhost/blog'

    MAIL_SERVER = 'smtp.googlemail.com'

    MAIL_PORT = 587

    MAIL_USE_TLS = True

    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")

    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):

	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:wati@localhost/blog'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:wati@localhost/blog'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
