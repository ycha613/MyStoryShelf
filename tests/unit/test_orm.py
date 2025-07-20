import pytest
from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError
from project.domainmodel.Movie import Movie, Genre
from project.domainmodel.User import User, MovieNote


# make functions

def make_movie():
    return Movie(id=1, title="A Movie", release_year=2023)

def make_user():
    return User("test", "Password123")

def make_genre():
    return Genre(id=1, name="Comedy")

def make_movienote():
    movie = make_movie()
    user = make_user()
    return MovieNote(movie=movie, user=user, note="a movie note")


# User orm tests and functions

def insert_user(empty_session, values=None):
    username = "test"
    password = "Password123"
    if values is not None:
        username = values[0]
        password = values[1]
    empty_session.execute(text('INSERT INTO users (username, password) VALUES (:username, :password)'),
                          {'username': username, 'password': password})
    row = empty_session.execute(text('SELECT user_id, username from users where username = :username'),
                                {'username': username}).fetchone()
    return row[0]

def insert_users(empty_session, values):
    for value in values:
        empty_session.execute(text('INSERT INTO users (username, password) VALUES (:username, :password)'),
                              {'username': value[0], 'password': value[1]})
    rows = list(empty_session.execute(text('SELECT username from users')))
    keys = tuple(row[0] for row in rows)
    return keys

def test_loading_of_users(empty_session):
    users = list()
    users.append(("username 1", "Password1"))
    users.append(("username 2", "Password2"))
    insert_users(empty_session, users)
    expected = [
        User("username 1", "Password1"),
        User("username 2", "Password2")
    ]
    assert empty_session.query(User).all() == expected

def test_saving_of_users(empty_session):
    user = make_user()
    empty_session.add(user)
    empty_session.commit()
    rows = list(empty_session.execute(text('SELECT username, password FROM users')))
    assert rows == [("test", "Password123")]

def test_saving_of_users_with_common_username(empty_session):
    insert_user(empty_session, ("test", "Password123"))
    empty_session.commit()
    with pytest.raises(IntegrityError):
        user = User("test", "Password233")
        empty_session.add(user)
        empty_session.commit()


# Movie orm tests and functions

def insert_movie(empty_session, values=None):
    movie_id, title, release_year = (1, "A Movie", 2023)
    if values is not None:
        movie_id, title, release_year = values
    empty_session.execute(text(
        'INSERT INTO movies (movie_id, title, release_year) VALUES (:movie_id, :title, :release_year)'),
        {'movie_id': movie_id, 'title': title, 'release_year': release_year}
    )
    row = empty_session.execute(text(
        'SELECT movie_id from movies where movie_id = :movie_id'),
        {'movie_id': movie_id}
    ).fetchone()
    return row[0]

def insert_movies(empty_session):
    empty_session.execute(text(
        'INSERT INTO movies (movie_id, title, release_year) VALUES (:movie_id, :title, :release_year)'),
        {'movie_id': 1, 'title': 'First Movie', 'release_year': 2024}
    )
    empty_session.execute(text(
        'INSERT INTO movies (movie_id, title, release_year) VALUES (:movie_id, :title, :release_year)'),
        {'movie_id': 2, 'title': 'Second Movie', 'release_year': 2023}
    )
    rows = list(empty_session.execute(text('SELECT movie_id from movies')))
    keys = tuple(row[0] for row in rows)
    return keys

def insert_movie_user_associations(empty_session, user_key, movie_keys):
    watched_stmt = text('INSERT into watched (user_id, movie_id) VALUES (:user_id, :movie_id)')
    watchlist_stmt = text('INSERT into watchlist (user_id, movie_id) VALUES (:user_id, :movie_id)')
    for movie_key in movie_keys:
        empty_session.execute(watched_stmt, {'user_id': user_key, 'movie_id': movie_key})
        empty_session.execute(watchlist_stmt, {'user_id': user_key, 'movie_id': movie_key})

def test_loading_of_movie(empty_session):
    movie_key = insert_movie(empty_session)
    expected_movie = make_movie()
    fetched_movie = empty_session.query(Movie).one()
    assert expected_movie == fetched_movie
    assert movie_key == fetched_movie.id

def test_saving_of_movie(empty_session):
    movie = make_movie()
    empty_session.add(movie)
    empty_session.commit()
    rows = list(empty_session.execute(text('SELECT movie_id, title FROM movies')))
    assert rows == [(1, 'A Movie')]

def test_saving_of_movies_with_common_id(empty_session):
    insert_movie(empty_session, (1, "Another Movie", 2023))
    empty_session.commit()
    with pytest.raises(IntegrityError):
        movie = Movie(1, "A Third Movie", 2022)
        empty_session.add(movie)
        empty_session.commit()

def test_loading_of_user_with_movies(empty_session):
    user_key = insert_user(empty_session)
    movie_keys = insert_movies(empty_session)
    insert_movie_user_associations(empty_session, user_key, movie_keys)
    user = empty_session.get(User, user_key)
    movies = [empty_session.get(Movie, key) for key in movie_keys]
    for movie in movies:
        assert movie in user.watched
        assert movie in user.watchlist

def test_saving_user_with_movies(empty_session):
    user = make_user()
    movie = make_movie()
    user.add_watched(movie)
    user.add_watchlist(movie)
    empty_session.add(user)
    empty_session.commit()
    rows = list(empty_session.execute(text('SELECT user_id FROM users')))
    user_key = rows[0][0]
    rows = list(empty_session.execute(text('SELECT movie_id, title FROM movies')))
    movie_key = rows[0][0]
    assert rows[0][1] == 'A Movie'
    rows = list(empty_session.execute(text('SELECT user_id, movie_id FROM watched')))
    user_foreign_key = rows[0][0]
    movie_foreign_key = rows[0][1]
    assert user_key == user_foreign_key
    assert movie_key == movie_foreign_key
    rows == list(empty_session.execute(text('SELECT user_id, movie_id FROM watchlist')))
    user_foreign_key = rows[0][0]
    movie_foreign_key = rows[0][1]
    assert user_key == user_foreign_key
    assert movie_key == movie_foreign_key

# Genre orm tests and functions

def insert_genres(empty_session):
    empty_session.execute(text(
        'INSERT INTO genres (genre_id, name) VALUES (:genre_id, :name)'),
        {'genre_id': 1, 'name': 'Comedy'}
    )
    empty_session.execute(text(
        'INSERT INTO genres (genre_id, name) VALUES (:genre_id, :name)'),
        {'genre_id': 2, 'name': 'Action'}
    )
    rows = list(empty_session.execute(text('SELECT genre_id from genres')))
    keys = tuple(row[0] for row in rows)
    return keys

def insert_movie_genre_associations(empty_session, movie_key, genre_keys):
    stmt = text('INSERT INTO movie_genres (movie_id, genre_id) VALUES (:movie_id, :genre_id)')
    for genre_key in genre_keys:
        empty_session.execute(stmt, {'movie_id': movie_key, 'genre_id': genre_key})

def test_loading_of_movie_with_genres(empty_session):
    movie_key = insert_movie(empty_session, (1, 'A Movie', 2023))
    genre_keys = insert_genres(empty_session)
    insert_movie_genre_associations(empty_session, movie_key, genre_keys)
    movie = empty_session.get(Movie, movie_key)
    genres = [empty_session.get(Genre, key) for key in genre_keys]
    for genre in genres:
        assert genre in movie.genres

def test_saving_movie_with_genres(empty_session):
    movie = make_movie()
    genre = make_genre()
    movie.add_genre(genre)
    empty_session.add(movie)
    empty_session.commit()
    rows = list(empty_session.execute(text('SELECT movie_id FROM movies')))
    movie_key = rows[0][0]
    rows = list(empty_session.execute(text('SELECT genre_id, name FROM genres')))
    genre_key = rows[0][0]
    assert rows[0][1] == 'Comedy'
    rows = list(empty_session.execute(text('SELECT movie_id, genre_id from movie_genres')))
    movie_foreign_key = rows[0][0]
    genre_foreign_key = rows[0][1]
    assert movie_key == movie_foreign_key
    assert genre_key == genre_foreign_key


# movie note orm tests and functions

def insert_movienote(empty_session):
    insert_movie(empty_session)
    insert_user(empty_session)
    empty_session.execute(text(
        'INSERT INTO movienotes (movie_id, user_id, note) VALUES (:movie_id, :user_id, :note)'),
        {"movie_id": 1, 'user_id': 1, 'note': 'a movie note'}
    )
    row = empty_session.execute(text(
        'SELECT id FROM movienotes where movie_id = :movie_id and user_id = :user_id'),
        {'movie_id': 1, 'user_id': 1}
    ).fetchone()
    return row[0]

def test_loading_of_movienote(empty_session):
    insert_movienote(empty_session)
    expected_movienote = [make_movienote()]
    assert expected_movienote == empty_session.query(MovieNote).all()

def test_saving_of_movienotes(empty_session):
    movienote = make_movienote()
    empty_session.add(movienote)
    empty_session.commit()
    rows = list(empty_session.execute(text(
        'SELECT movie_id, user_id, note FROM movienotes'
    )))
    assert rows == [(1, 1, 'a movie note')]