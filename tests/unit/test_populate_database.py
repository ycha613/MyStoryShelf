import pytest
from sqlalchemy import select, inspect
from sqlalchemy.orm import sessionmaker
from project.adapters.orm import mapper_registry
from project.domainmodel.Movie import Movie, Genre
from project.domainmodel.User import User, MovieNote

def test_populate_database(database_engine):
    inspector = inspect(database_engine)
    assert inspector.get_table_names() == [
        'genres', 'movie_genres', 'movienotes', 'movies', 'users', 'watched', 'watchlist'
    ]
    Session = sessionmaker(bind=database_engine)
    session = Session()
    assert session.query(Movie).count() == 98, "Movies tables should be populated"
    assert session.query(Genre).count() == 17, "Genres tables should be populated"
    session.close()