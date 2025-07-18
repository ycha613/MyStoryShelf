import pytest
from project.domainmodel.User import User, MovieNote
from project.domainmodel.Movie import Movie, Genre

@pytest.fixture
def my_user():
    return User(username="john", password="Password123")

@pytest.fixture
def my_movie():
    return Movie(id=10101, title="Psycho", release_year=1960)