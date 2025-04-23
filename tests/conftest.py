import pytest
from project.domainmodel.User import User
from project.domainmodel.Media import Movie, Book, Show

@pytest.fixture
def my_user():
    return User(username="john", password="Password123")

@pytest.fixture
def my_movie():
    return Movie(title="Psycho", user=my_user, director="Alfred Hitchock")

@pytest.fixture
def my_show():
    return Show(title="Breaking Bad", user=my_user, season=1)

@pytest.fixture
def my_book():
    return Book(title="Moby Dick", user=my_user, author="Herman Melville")