from flask import Blueprint, render_template
import project.adapters.repository as repo
import project.browse.services as services

browse_blueprint = Blueprint("browse_bp", __name__)

@browse_blueprint.route("/movies/<int:page_id>", methods=["GET"])
def browse(page_id):
    movies = services.get_movies_by_page(repo.repo_instance, page_id)
    last_page = services.get_total_pages(repo.repo_instance)

    return render_template("browse.html", movies=movies, page_id=page_id,
                           last_page=last_page)