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
        self._notes = list()
        
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
    
    @property
    def notes(self) -> list[MovieNote]:
        return self._notes.copy()
    
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

    def add_notes(self, note: MovieNote):
        self._notes.append(note)
    
    def remove_notes(self, note: MovieNote):
        self._notes.remove(note)
    
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
    

class MovieNote:
    def __init__(self, movie: Movie, user: User, note: str):
        if not isinstance(movie, Movie):
            raise TypeError("the movie must be a movie object")
        self._movie = movie
        if not isinstance(user, User):
            raise TypeError("the user must be a user object")
        self._user = user
        self._note = note

    @property
    def movie(self) -> Movie:
        return self._movie
    
    @property
    def user(self) -> User:
        return self._user
    
    @property
    def note(self) -> str:
        return self._note
    
    @note.setter
    def note(self, new_note: str):
        self._note = new_note

    def __eq__(self, other) -> bool:
        if not isinstance(other, MovieNote):
            return False
        return self._movie == other._movie and self._user == other._user and self._note == other._note
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, MovieNote):
            return False
        if self._movie == other._movie:
            return self._note < other._note
        return self._movie < other._movie
    
    def __hash__(self) -> int:
        return hash(repr(self._movie) + repr(self._user) + self._note)
    
    def __repr__(self) -> str:
        return f"<MovieNote by {self.user.username} on {self.movie.title}>"
        