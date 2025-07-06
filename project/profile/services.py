from project.adapters.repository import AbstractRepository
from project.domainmodel.Movie import Movie
from project.domainmodel.User import User

def get_user(username: str, repo: AbstractRepository) -> User:
    return repo.get_user(user_name=username)