import pytest
from project.domainmodel.Movie import Movie, Genre
from project.domainmodel.User import User, MovieNote
from project.adapters.csv_reader import MovieCSVReader
from project.adapters.database_repository import DatabaseRepository

"""
Unit tests for the repository layer of the application
"""

def test_drepo_user_methods(session_factory, my_movie):
    # add_user(user) method
    # get_user(username) method
    repo = DatabaseRepository(session_factory)
    user = User("testuser", "Password123")
    repo.add_user(user)
    retrieved_user = repo.get_user("testuser")
    assert retrieved_user == user

    # update_user(user) method
    user.add_watched(my_movie)
    repo.update_user(user)
    retrieved_user = repo.get_user("testuser")
    assert my_movie in retrieved_user.watched


def test_drepo_movie_methods(session_factory, my_movie, my_user):
    # get movies_by_page(page_number) method
    # get_movie_by_id(id) method)
    repo = DatabaseRepository(session_factory)
    assert len(repo.get_movies_by_page(1)[0]) == 40
    assert repo.get_movies_by_page(1)[1] == 3
    assert my_movie not in repo.get_movies_by_page(1)[0]

    # add_movie(movie) method
    repo.add_movie(my_movie)
    assert my_movie in repo.get_movies_by_page(1)[0]
    retrieved_movie = repo.get_movie_by_id(my_movie.id)
    assert retrieved_movie == my_movie

    # add_movies(movies) method
    movie2 = Movie(id=2010010, title="A movie", release_year=2024)
    movie3 = Movie(id=2020202, title="Another movie", release_year=2024)
    movies = [movie2, movie3]
    repo.add_movies(movies)
    assert movie2 in repo.get_movies_by_page(1)[0]
    assert movie3 in repo.get_movies_by_page(1)[0]


def test_drepo_search_methods(session_factory):
    # search_movies_by_title(search_term, page_number)
    repo = DatabaseRepository(session_factory)
    movies, pages = repo.search_movies_by_title("La La Land", 1)
    assert pages == 1
    assert len(movies) == 1
    assert movies[0].title == "La La Land"

    # search_movies_by_release_year(search_term, page_number)
    movies, pages = repo.search_movies_by_release_year(1999, 1)
    assert pages == 1
    assert len(movies) == 2
    assert movies[0].title == "Fight Club"
    assert movies[1].title == "The Matrix"

    # search_movies_by_genre(search_term, page_number)
    movies, pages = repo.search_movies_by_genre("Drama", 1)
    assert pages == 2
    assert len(movies) == 40
    assert movies[0].title == "Challengers"
