"""
Initialize the flask app
"""

from flask import Flask
import os

def create_app():
    app = Flask(
        __name__, 
        template_folder=os.path.join(os.path.dirname(__file__), "templates")
    )

    with app.app_context():
        # register blueprints
        from .home import home
        app.register_blueprint(home.home_blueprint)
        pass

    return app