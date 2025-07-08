from __future__ import annotations
from project.domainmodel.Movie import Movie

def validate_username(username: str):
    if not isinstance(username, str):
        raise TypeError("Username must be a string.")
    
    if len(username.strip()) < 3:
        raise ValueError("Username must be at least 3 characters long.")

def validate_password(password: str):
    if not isinstance(password, str):
        raise TypeError("Password must be a string.")
    
    if len(password.strip()) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    has_uppercase = has_lowercase = has_digit = False

    for c in password:
        if c.isupper(): has_uppercase = True
        if c.islower(): has_lowercase = True
        if c.isdigit(): has_digit = True
    if (has_uppercase == False or has_lowercase == False or has_digit == False):
        raise ValueError("Password must have at least one uppercase, one lowercase and one digit.")


class User():
    def __init__(self, username: str, password: str):
        validate_username(username)
        self._username = username
        validate_password(password)
        self._password = password
        self._watched = list()
        self._watchlist = list()
        
    @property
    def username(self) -> str:
        return self._username
    
    @property
    def password(self) -> str:
        return self._password
    
    @property
    def watched(self) -> list[Movie]:
        return self._watched.copy()
    
    @property
    def watchlist(self) -> list[Movie]:
        return self._watchlist.copy()
    
    def add_watched(self, movie: Movie):
        if movie not in self._watched:
            self._watched.append(movie)

    def remove_watched(self, movie: Movie):
        if movie in self._watched:
            self._watched.remove(movie)

    def add_watchlist(self, movie: Movie):
        if movie not in self._watchlist:
            self._watchlist.append(movie)
    
    def remove_watchlist(self, movie: Movie):
        if movie in self._watchlist:
            self._watchlist.remove(movie)
    
    def __repr__(self) -> str:
        return f"<User: {self.username}>"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return False
        return self.username == other.username
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, User):
            return False
        return self.username < other.username
    
    def __hash__(self) -> int:
        return hash(self.username)