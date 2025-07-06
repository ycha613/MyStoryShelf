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
        self._page_size = 20

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    # implement relevant methods in abstract repository

    def get_user(self, user_name: str) -> User:
        user = None
        try:
            user = self._session_cm.session.query(User).filter(User._username == user_name).one()
        except NoResultFound:
            pass
        return user
    
    def add_user(self, user: User):
        with self._session_cm as scm:
            scm.session.add(user)
            scm.commit()

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

    def get_total_pages(self) -> int:
        with self._session_cm as scm:
            total_movies = scm.session.query(Movie).count()
            return (total_movies + self._page_size - 1) // self._page_size
        
    def get_movies_by_page(self, page_number: int) -> list[Movie]:
        max_page_number = self.get_total_pages()
        if page_number < 1 or page_number > max_page_number:
            raise ValueError("Page number is invalid.")
        
        with self._session_cm as scm:
            offset = (page_number - 1) * self._page_size
            stmt = select(Movie).order_by(
                Movie._release_year.desc(), 
                Movie._title.asc()
                ).offset(offset).limit(self._page_size)
            result = scm.session.execute(stmt).scalars().all()
            return result
        
    def get_movie_by_id(self, movie_id: int) -> Movie:
        movie = None
        try:
            movie = self._session_cm.session.query(Movie).filter(Movie._id == movie_id).one()
        except NoResultFound:
            pass
        return movie




def database_repository_populate(csvreader: MovieCSVReader, repo: DatabaseRepository):
    csvreader.read_files()
    repo.add_movies(csvreader._movies.values())