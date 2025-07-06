from flask import Blueprint, render_template
from project.helpers import get_username

home_blueprint = Blueprint("home_bp", __name__)

@home_blueprint.route("/", methods=["GET"])
def home():
    username = get_username()
    return render_template("home.html", username=username)