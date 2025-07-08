from flask import Blueprint, render_template, jsonify
import project.adapters.repository as repo
import project.profile.services as services
from project.helpers import get_username
from project.authentication.authentication import login_required

profile_blueprint = Blueprint("profile_bp", __name__)

@profile_blueprint.route("/profile/<string:username>", methods=["GET"])
def profile(username):
    # get user object, make sure watched and watchlist eagerly loaded
    user = services.get_user(repo=repo.repo_instance, username=username)
    print(user.watched)

    return render_template("profile.html", user=user, username=username)


@profile_blueprint.route("/toggle_watchlist/<int:movie_id>", methods=["POST"])
@login_required
def toggle_watchlist(movie_id):
    username = get_username()
    # possible that watchlist and watched not eagerly loaded?
    user = services.get_user(repo=repo.repo_instance, username=username)
    movie = services.get_movie_by_id(repo=repo.repo_instance, movie_id=movie_id)

    in_list = False
    if movie in user.watchlist:
        user.remove_watchlist(movie)
    else:
        user.add_watchlist(movie)
        in_list = True

    services.update_user(repo=repo.repo_instance, user=user)
    
    json_payload = {"success": True, "in_list": in_list}
    return jsonify(json_payload)


@profile_blueprint.route("/toggle_watched/<int:movie_id>", methods=["POST"])
@login_required
def toggle_watched(movie_id):
    username = get_username()
    # possible that watchlist and watched not eagerly loaded?
    user = services.get_user(repo=repo.repo_instance, username=username)
    movie = services.get_movie_by_id(repo=repo.repo_instance, movie_id=movie_id)

    in_list = False
    if movie in user.watched:
        user.remove_watched(movie)
    else:
        user.add_watched(movie)
        in_list = True

    services.update_user(repo=repo.repo_instance, user=user)
    
    json_payload = {"success": True, "in_list": in_list}
    return jsonify(json_payload)

