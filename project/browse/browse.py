from flask import Blueprint, render_template, session, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
import project.adapters.repository as repo
import project.browse.services as services
from project.helpers import get_username

browse_blueprint = Blueprint("browse_bp", __name__)

@browse_blueprint.route("/movies", methods=["GET"])
def browse():
    try:
        page_id = int(request.args.get("page_id", 1))
        if page_id < 1:
            page_id = 1
    except:
        page_id = 1
    
    form = SearchForm(request.args)
    search_type = form.search_type.data or 'title'
    search_term = form.search_term.data or ''
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

class SearchForm(FlaskForm):
    search_type = SelectField(
        'Search by:',
        choices=[('title', 'Title'), ('genre','Genre'), ('release year', 'Release Year')],
        validators=[DataRequired()]
    )
    search_term = StringField('Enter search term', validators=[DataRequired()])
    submit = SubmitField('🔍')


@browse_blueprint.route("/movie/<int:movie_id>", methods=["GET", "POST"])
def movie(movie_id):
    form = MovieNoteForm()
    movie = services.get_movie_by_id(repo.repo_instance, movie_id)
    username = get_username()
    user = services.get_user(repo.repo_instance, username)

    if form.validate_on_submit():
        services.add_movie_note(repo=repo.repo_instance, movie=movie, user=user, note=form.note.data)
        return redirect(url_for('browse_bp.movie', movie_id=movie_id))

    notes = None
    if user:
        notes = [note for note in user.notes if note.movie == movie]

    return render_template("movie.html", movie=movie, username=username, user=user, 
                           form=form, notes=notes)

class MovieNoteForm(FlaskForm):
    note = TextAreaField('Note', validators=[DataRequired()])
    submit = SubmitField('Add Note')