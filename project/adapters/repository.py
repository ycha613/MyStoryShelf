from abc import ABC, abstractmethod
from project.domainmodel.User import User
from project.domainmodel.Movie import Movie, Genre

repo_instance = None


class AbstractRepository(ABC):
    @abstractmethod
    def add_movie(self):
        raise NotImplementedError
    
    @abstractmethod
    def add_movies(self):
        raise NotImplementedError