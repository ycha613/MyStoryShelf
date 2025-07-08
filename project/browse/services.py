from project.adapters.repository import AbstractRepository
from project.domainmodel.Movie import Movie
from project.domainmodel.User import User

"""
Services for the browse blueprint
"""

def get_movies_by_page(repo: AbstractRepository, page_number: int) -> list[Movie]:
    return repo.get_movies_by_page(page_number=page_number)

def get_total_pages(repo: AbstractRepository) -> int:
    return repo.get_total_pages()

def get_movie_by_id(repo: AbstractRepository, movie_id: int) -> Movie:
    return repo.get_movie_by_id(movie_id=movie_id)

def get_user(repo: AbstractRepository, username: str) -> User:
    return repo.get_user(user_name=username)