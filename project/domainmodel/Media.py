from __future__ import annotations
import project.domainmodel.User as User


class Media:
    def __init__(self, title: str, user: User.User):
        self._id = None
        adj_title = " ".join([a.capitalize() for a in title.strip().split()])
        self._title = adj_title
        self._user = user

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def user(self) -> User.User:
        return self._user
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.title}>"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        else:
            return self._title.lower() == other._title.lower()
        
    def __lt__(self, other) -> bool:
        if not isinstance(other, Media):
            return False
        else:
            return self._title.lower() < other._title.lower()
        
    def __hash__(self) -> int:
        return hash(self._title.lower())


class Book(Media):
    def __init__(self, title: str, user: User.User, author: str):
        super().__init__(title, user)
        adj_author = " ".join([a.capitalize() for a in author.strip().split()])
        self._author = adj_author

    @property
    def author(self) -> str:
        return self._author

   
class Movie(Media):
    def __init__(self, title: str, user: User.User, director: str):
        super().__init__(title, user)
        adj_director = " ".join([a.capitalize() for a in director.strip().split()])
        self._director = adj_director

    @property
    def director(self) -> str:
        return self._director


class Show(Media):
    def __init__(self, title: str, user: User.User, season: int):
        super().__init__(title, user)
        self._season = season
    
    @property
    def season(self) -> int:
        return self._season