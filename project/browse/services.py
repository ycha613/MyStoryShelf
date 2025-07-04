from project.adapters.repository import AbstractRepository
from project.domainmodel.Movie import Movie

"""
Services for the browse blueprint
"""

def get_movies_by_page(repo: AbstractRepository, page_number: int) -> list[Movie]:
    return repo.get_movies_by_page(page_number)

def get_total_pages(repo: AbstractRepository) -> int:
    return repo.get_total_pages()