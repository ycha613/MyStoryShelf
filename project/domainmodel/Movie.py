from __future__ import annotations

# validation functions
def validate_string(s: str):
    if not isinstance(s, str):
        raise TypeError("This field must be a string.")
    if len(s.strip()) <= 0:
        raise ValueError("The field must be non empty.")
    

# not used for now
class Director:
    def __init__(self, name: str):
        self._id = None
        validate_string(name)
        self._name = name

    @property
    def name(self) -> str:
        return self._name


class Genre:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name


class Movie:
    def __init__(self, id: int, title: str,
                 release_year: int = None, description: str = "", 
                 runtime: int = -1):
        self._id = id
        validate_string(title)
        self._title = title
        self._poster_link = None
        self._release_year = release_year
        self._description = description
        self._runtime = runtime
        self._genres = list()

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def poster_link(self) -> str:
        return self._poster_link
    
    @poster_link.setter
    def poster_link(self, new_poster_link: str):
        self._poster_link = new_poster_link
    
    @property
    def release_year(self) -> int:
        return self._release_year
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def runtime(self) -> int:
        return self._runtime
    
    @property
    def genres(self) -> []:
        return self._genres.copy()
    
    def add_genre(self, genre: Genre):
        if genre not in self._genres:
            self._genres.append(genre)
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Movie):
            return False
        return self._title == other._title
    
    def __hash__(self) -> int:
        return hash(self._title + self.__class__.__name__)
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.title}>"
        
    def __lt__(self, other) -> bool:
        if not isinstance(other, Movie):
            return False
        return self._title < other._title
