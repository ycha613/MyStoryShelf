import pytest
from project.domainmodel.User import User, MovieNote
from project.domainmodel.Movie import Movie, Genre

"""
Unit tests for the domain model of the web application
"""

# User class unit tests

def test_user_initialisation():
    user1 = User("john", "Password1")
    assert repr(user1) == "<User: john>"
    assert user1.username == "john"
    assert user1.password == "Password1"

    with pytest.raises(TypeError):
        user2 = User(1, "Password1")
    with pytest.raises(TypeError):
        user2 = User("john", 1)

    with pytest.raises(ValueError):
        user2 = User("", "Password1")
    with pytest.raises(ValueError):
        user2 = User("john", "")

def test_user_eq():
    user1 = User("aaron", "Password1")
    user2 = User("aaron", "Password2")
    user3 = User("chris", "Password3")
    assert user1 == user2
    assert user1 != user3
    assert user3 == user3

def test_user_lt():
    user1 = User("aaron", "Password1")
    user2 = User("brian", "Password2")
    user3 = User("chris", "Password3")
    assert user1 < user2 < user3
    user_list = [user3, user2, user1]
    assert sorted(user_list) == [user1, user2, user3]

def test_user_hash():
    user1 = User("aaron", "Password1")
    user2 = User("brian", "Password2")
    user3 = User("chris", "Password3")
    user_set = set()
    user_set.add(user1)
    user_set.add(user2)
    user_set.add(user3)
    
    assert len(user_set) == 3
    assert repr(sorted(user_set)) == "[<User: aaron>, <User: brian>, <User: chris>]"
    user_set.discard(user1)
    assert repr(sorted(user_set)) == "[<User: brian>, <User: chris>]"


# Genre class unit tests

def test_genre_initialisation():
    genre1 = Genre(id=1, name="Comedy")
    assert repr(genre1) == "<Genre 1: Comedy>"
    assert genre1.name == "Comedy"
    assert genre1.id == 1
    with pytest.raises(TypeError):
        genre2 = Genre(2, 300)

def test_genre_eq():
    genre1 = Genre(id=1, name="Comedy")
    genre2 = Genre(id=2, name="Action")
    genre3 = Genre(id=3, name="Indie")
    assert genre1 == genre1
    assert genre1 != genre2
    assert genre2 != genre3

def test_genre_lt():
    genre1 = Genre(id=1, name="Comedy")
    genre2 = Genre(id=2, name="Action")
    genre3 = Genre(id=3, name="Indie")
    assert genre1 > genre2
    assert genre1 < genre3
    assert genre2 < genre3
    genre_list = [genre1, genre2, genre3]
    assert sorted(genre_list) == [genre2, genre1, genre3]

def test_genre_hash():
    genre1 = Genre(id=1, name="Comedy")
    genre2 = Genre(id=2, name="Action")
    genre3 = Genre(id=3, name="Indie")
    genre_set = set()
    genre_set.add(genre1)
    genre_set.add(genre2)
    genre_set.add(genre3)
    assert len(genre_set) == 3


# Movie class unit tests

def test_movie_initialisation():
    movie1 = Movie(id=10101, title="Psycho", release_year=1960)
    assert repr(movie1) == "<Movie: Psycho>"
    assert movie1.id == 10101
    assert movie1.title == "Psycho"
    assert movie1.release_year == 1960
    assert movie1.runtime == -1
    assert movie1.description == ""

    with pytest.raises(TypeError):
        movie1 = Movie(id=10101, title=3, release_year=1960)
    with pytest.raises(TypeError):
        movie1 = Movie(id="10101", title="Psycho", release_year=1960)

    with pytest.raises(ValueError):
        movie1 = Movie(id=10101, title="", release_year=1960)

def test_movie_eq():
    movie1 = Movie(id=10101, title="Psycho", release_year=1960)
    movie2 = Movie(id=10101, title="Psycho", release_year=1960)
    movie3 = Movie(id=10102, title="Vertigo", release_year=1950)
    movie4 = Movie(id=10101, title="Vertigo", release_year=1965)
    assert movie1 == movie2
    assert movie1 != movie3
    assert movie1 == movie4
    assert movie4 == movie4

def test_movie_lt():
    movie1 = Movie(id=10101, title="Psycho", release_year=1960)
    movie2 = Movie(id=10102, title="Stage Fright", release_year=1960)
    movie3 = Movie(id=10103, title="Vertigo", release_year=1960)
    movies_list = [movie3, movie2, movie1]
    assert movie1 < movie2 < movie3
    assert sorted(movies_list) == [movie1, movie2, movie3]


def test_movie_hash():
    movie1 = Movie(id=10101, title="Psycho", release_year=1960)
    movie2 = Movie(id=10102, title="Stage Fright", release_year=1960)
    movie3 = Movie(id=10103, title="Vertigo", release_year=1960)
    movies_set = set()
    movies_set.add(movie1)
    movies_set.add(movie2)
    movies_set.add(movie3)
    assert len(movies_set) == 3


# MovieNote class unit tests

def test_movienote_initialisation(my_movie, my_user):
    movienote = MovieNote(movie=my_movie, user=my_user, note="test")
    assert repr(movienote) == "<MovieNote by john on Psycho>"
    with pytest.raises(TypeError):
        movienote = MovieNote(movie="Psycho", user=my_user, note="test")
    with pytest.raises(TypeError):
        movienote = MovieNote(movie=my_movie, user="john", note="test")

def test_movienote_eq(my_movie, my_user):
    movienote1 = MovieNote(movie=my_movie, user=my_user, note="test")
    movienote2 = MovieNote(movie=my_movie, user=my_user, note="test2")
    assert movienote1 == movienote1
    assert movienote1 != movienote2

def test_movienote_lt(my_movie, my_user):
    movie2 = Movie(id=10102, title="Stage Fright", release_year=1960)
    movienote1 = MovieNote(movie=my_movie, user=my_user, note="test")
    movienote2 = MovieNote(movie=my_movie, user=my_user, note="test2")
    movienote3 = MovieNote(movie=movie2, user=my_user, note="test")
    assert movienote1 < movienote2
    assert movienote1 < movienote3
    assert movienote2 < movienote3

def test_movienote_hash(my_movie, my_user):
    movienote1 = MovieNote(movie=my_movie, user=my_user, note="test")
    movienote2 = MovieNote(movie=my_movie, user=my_user, note="test2")
    movienote3 = MovieNote(movie=my_movie, user=my_user, note="test3")
    movienotes_set = set()
    movienotes_set.add(movienote1)
    movienotes_set.add(movienote2)
    movienotes_set.add(movienote3)
    assert len(movienotes_set) == 3