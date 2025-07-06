from flask import Blueprint, render_template
import project.adapters.repository as repo
import project.profile.services as services
from project.helpers import get_username

profile_blueprint = Blueprint("profile_bp", __name__)

@profile_blueprint.route("/profile/<string:username>", methods=["GET"])
def profile(username):
    # get user object, make sure watched and watchlist eagerly loaded
    user = services.get_user(repo=repo.repo_instance, username=username)

    return render_template("profile.html", user=user, username=username)

