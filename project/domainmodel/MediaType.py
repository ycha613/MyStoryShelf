from enum import Enum
from sqlalchemy import Enum as SqlEnum

class MediaType(Enum):
    MOVIE = "movie"
    BOOK = "book"
    SHOW = "show"
    MANGA = "manga"