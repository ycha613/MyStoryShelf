""" Flask configuration variables """
from os import environ
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    SECRET_KEY = environ.get("SECRET_KEY")
    TESTING = environ.get("TESTING")

    # Database
    #print(environ.get("SQLALCHEMY_DATABASE_URI"))
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    echo_string = environ.get("SQLALCHEMY_ECHO")
    SQLALCHEMY_ECHO = False
    if echo_string.lower().strip() == "true":
        SQLALCHEMY_ECHO= True