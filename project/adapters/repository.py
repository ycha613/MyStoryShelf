from abc import ABC, abstractmethod
from project.domainmodel.User import User
from project.domainmodel.Movie import Movie, Genre

repo_instance = None


class AbstractRepository(ABC):
    @abstractmethod
    def get_user(self, user_name: str) -> User:
        raise NotImplementedError
    
    @abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError
    
    @abstractmethod
    def update_user(self, user: User):
        raise NotImplementedError

    @abstractmethod
    def add_movie(self):
        raise NotImplementedError
    
    @abstractmethod
    def add_movies(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_total_pages(self) -> int:
        raise NotImplementedError
    
    @abstractmethod
    def get_movies_by_page(self, page_number: int) -> tuple[list[Movie], int]:
        raise NotImplementedError
    
    @abstractmethod
    def search_movies_by_genre(self, search_term: str, page_number: int) -> tuple[list[Movie], int]:
        raise NotImplementedError
    
    @abstractmethod
    def search_movies_by_title(self, search_term: str, page_number: int) -> tuple[list[Movie], int]:
        raise NotImplementedError
    
    @abstractmethod
    def search_movies_by_release_year(self, search_term: str, page_number: int) -> tuple[list[Movie], int]:
        raise NotImplementedError
    
    @abstractmethod
    def get_movie_by_id(self, movie_id: int) -> Movie:
        raise NotImplementedError