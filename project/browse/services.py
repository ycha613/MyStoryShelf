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

def search_movies_by_genre(repo: AbstractRepository, search_term: str, page_number: int) -> list[Movie]:
    return repo.search_movies_by_genre(search_term=search_term, page_number=page_number)

def search_movies_by_title(repo: AbstractRepository, search_term: str, page_number: int) -> list[Movie]:
    return repo.search_movies_by_title(search_term=search_term, page_number=page_number)

def search_movies_by_release_year(repo: AbstractRepository, search_term: str, page_number: int) -> list[Movie]:
    return repo.search_movies_by_release_year(search_term=search_term, page_number=page_number)

def add_movie_note(repo: AbstractRepository, movie: Movie, user: User, note: str):
    repo.add_movie_note(movie=movie, user=user, note=note)