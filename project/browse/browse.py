from flask import Blueprint, render_template, session
import project.adapters.repository as repo
import project.browse.services as services
from project.helpers import get_username

browse_blueprint = Blueprint("browse_bp", __name__)

@browse_blueprint.route("/movies/<int:page_id>", methods=["GET"])
def browse(page_id):
    movies = services.get_movies_by_page(repo.repo_instance, page_id)
    last_page = services.get_total_pages(repo.repo_instance)

    username = get_username()
    return render_template("browse.html", movies=movies, page_id=page_id,
                           last_page=last_page, username=username)


@browse_blueprint.route("/movie/<int:movie_id>", methods=["GET"])
def movie(movie_id):
    movie = services.get_movie_by_id(repo.repo_instance, movie_id)

    username = get_username()
    return render_template("movie.html", movie=movie, username=username)