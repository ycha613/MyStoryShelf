import pytest
from project.domainmodel.User import User, MovieNote
from project.domainmodel.Movie import Movie, Genre

@pytest.fixture
def my_user():
    return User(username="john", password="Password123")

@pytest.fixture
def my_movie():
    return Movie(id=10101, title="Psycho", release_year=1960)

@pytest.fixture
def my_genre():
    return Genre(id=1, name="Action")

@pytest.fixture
def my_movienote(my_movie, my_user):
    return MovieNote(movie=my_movie, user=my_user, note="test")