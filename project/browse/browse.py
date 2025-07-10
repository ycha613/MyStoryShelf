from flask import Blueprint, render_template, session, request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
import project.adapters.repository as repo
import project.browse.services as services
from project.helpers import get_username

browse_blueprint = Blueprint("browse_bp", __name__)

@browse_blueprint.route("/movies/<int:page_id>", methods=["GET"])
def browse(page_id):
    form = SearchForm(request.args)
    search_type = form.search_type.data or 'title'
    search_term = form.search_term.data or ''
    print(search_term, search_type)
    if search_term.strip() != '':
        if search_type == 'title':
            movies, max_page = services.search_movies_by_title(repo.repo_instance, search_term, page_id)
        elif search_type == 'genre':
            movies, max_page = services.search_movies_by_genre(repo.repo_instance, search_term, page_id)
        elif search_type == 'release year':
            movies, max_page = services.search_movies_by_release_year(repo.repo_instance, search_term, page_id)
        else:
            movies, max_page = services.get_movies_by_page(repo.repo_instance, page_id)
    else:
        movies, max_page = services.get_movies_by_page(repo.repo_instance, page_id)
    username = get_username()
    return render_template("browse.html", movies=movies, page_id=page_id, form=form, max_page=max_page,
                            username=username, search_term=search_term, search_type=search_type)


@browse_blueprint.route("/movie/<int:movie_id>", methods=["GET"])
def movie(movie_id):
    movie = services.get_movie_by_id(repo.repo_instance, movie_id)

    username = get_username()
    user = services.get_user(repo.repo_instance, username)
    return render_template("movie.html", movie=movie, username=username, user=user)


class SearchForm(FlaskForm):
    search_type = SelectField(
        'Search by:',
        choices=[('title', 'Title'), ('genre','Genre'), ('release year', 'Release Year')],
        validators=[DataRequired()]
    )
    search_term = StringField('Enter search term', validators=[DataRequired()])
    submit = SubmitField('🔍')