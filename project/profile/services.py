from project.adapters.repository import AbstractRepository
from project.domainmodel.Movie import Movie
from project.domainmodel.User import User

def get_user(username: str, repo: AbstractRepository) -> User:
    return repo.get_user(user_name=username)

def get_movie_by_id(repo: AbstractRepository, movie_id: int) -> Movie:
    return repo.get_movie_by_id(movie_id=movie_id)

def update_user(repo: AbstractRepository, user: User):
    repo.update_user(user)