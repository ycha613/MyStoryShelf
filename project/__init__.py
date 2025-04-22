"""
Initialize the flask app
"""

from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="project/templates")

    with app.app_context():
        # register blueprints
        pass

    return app