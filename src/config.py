import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ho-ho-ho-hooo'
    SQLALCHEMY_DATABASE_URI =  "postgresql://hello_flask:hello_flask@db:5432/hello_flask_dev"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
