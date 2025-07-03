from __future__ import annotations
from project.domainmodel.User import User


def validate_string(s: str):
    if not isinstance(s, str):
        raise TypeError("This field must be a string.")
    if len(s.strip()) <= 0:
        raise ValueError("The field must be non empty.")
    
def validate_positive_int(i: int):
    if not isinstance(i, int):
        raise TypeError("This field must be a integer.")
    if i <= 0:
        raise ValueError("This field must be a positive integer.")


class Media:
    def __init__(self, title: str, user: User):
        self._id = None
        validate_string(title)
        adj_title = " ".join([a.capitalize() for a in title.strip().split()])
        self._title = adj_title
        if not isinstance(user, User):
            raise TypeError("User must be a User object.")
        self._user = user

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def user(self) -> User:
        return self._user
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.title}>"
        
    def __lt__(self, other) -> bool:
        if not isinstance(other, Media):
            return False
        return self._title < other._title


class Book(Media):
    def __init__(self, title: str, user: User, author: str):
        super().__init__(title, user)
        validate_string(author)
        adj_author = " ".join([a.capitalize() for a in author.strip().split()])
        self._author = adj_author

    @property
    def author(self) -> str:
        return self._author
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return self._title == other._title and self._author == other._author
        
    def __hash__(self) -> int:
        return hash(self._title + self._author + self.__class__.__name__)


class Show(Media):
    def __init__(self, title: str, user: User, season: int):
        super().__init__(title, user)
        validate_positive_int(season)
        self._season = season
    
    @property
    def season(self) -> int:
        return self._season
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Show):
            return False
        return self._title == other._title and self._season == other._season
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, Media):
            return False
        if isinstance(other, Show) and self._title == other._title:
            return self._season < other._season
        return self._title < other._title
        
    def __hash__(self) -> int:
        return hash(self._title + str(self._season) + self.__class__.__name__)