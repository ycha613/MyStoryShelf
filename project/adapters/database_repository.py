from sqlalchemy import desc, asc
from sqlalchemy import select
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from project.domainmodel.User import User
from project.domainmodel.Movie import Movie, Genre
from project.adapters.repository import AbstractRepository
from project.adapters.csv_reader import MovieCSVReader


class SessionContextManager:
    def __init__(self, session_factory):
        self._session_factory = session_factory
        self._session = scoped_session(self._session_factory)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self._session

    def rollback(self):
        self._session.rollback()

    def commit(self):
        self._session.commit()

    def close_current_session(self):
        if not self._session is None:
            self._session.close()

    def reset_session(self):
        self.close_current_session()
        self._session = scoped_session(self._session_factory)


class DatabaseRepository(AbstractRepository):
    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    # implement relevant methods in abstract repository

    def add_movie(self, movie: Movie):
        if not movie or not isinstance(movie, Movie): return
        with self._session_cm as scm:
            scm.session.add(movie)
            scm.commit()

    def add_movies(self, movies: list[Movie]):
        if not movies: return
        with self._session_cm as scm:
            for movie in movies:
                if isinstance(movie, Movie): scm.session.add(movie)
            scm.commit()



def database_repository_populate(csvreader: MovieCSVReader, repo: DatabaseRepository):
    csvreader.read_files()
    repo.add_movies(csvreader._movies.values())