from flask import Blueprint, render_template

browse_blueprint = Blueprint("browse_bp", __name__)

@browse_blueprint.route("/movies/<int:page_id>", methods=["GET"])
def browse():
    # get movies

    # pagination calculations

    return render_template("home.html")