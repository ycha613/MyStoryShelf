from __future__ import annotations
from project.domainmodel.Movie import Movie, Genre
import csv

class MovieCSVReader:
    def __init__(self, movies_file: str, genres_file: str, posters_file: str):
        self._movies_file = movies_file
        self._genres_file = genres_file
        self._posters_file = posters_file
        self._movies = dict()
        self._genres = dict()

    def read_files(self, stopping_id = None):
        with open(self._movies_file, 'r') as movies_file:
            movies_reader = csv.reader(movies_file)
            next(movies_reader)
            for row in movies_reader:
                try:
                    id = int(row[0])
                    title = row[1]
                    date = int(row[2])
                    description = row[4]
                    runtime = (-1 if row[5] == "" else int(row[5]))
                    if (stopping_id is not None and id > stopping_id):
                        break
                    new_movie = Movie(id=id, title=title, release_year=date,
                                    description=description, runtime=runtime)
                    self._movies[id] = new_movie
                except (ValueError, IndexError):
                    continue
        
        with open(self._posters_file, 'r') as posters_file:
            posters_reader = csv.reader(posters_file)
            next(posters_reader)
            for row in posters_reader:
                try:
                    id = int(row[0])
                    poster_link = row[1]
                    if (stopping_id is not None and id > stopping_id):
                        break
                    movie = self._movies.get(id)
                    if movie: movie.poster_link = poster_link
                except (ValueError, IndexError):
                    continue
        
        with open(self._genres_file, 'r') as genres_file:
            id_counter = 1
            genres_reader = csv.reader(genres_file)
            next(genres_reader)
            for row in genres_reader:
                try:
                    id = int(row[0])
                    genre_name = row[1]
                    if (stopping_id is not None and id > stopping_id):
                        break
                    if genre_name not in self._genres.keys():
                        new_genre = Genre(id=id_counter, name=genre_name)
                        id_counter += 1
                        self._genres[genre_name] = new_genre
                    genre = self._genres[genre_name]
                    movie = self._movies.get(id)
                    if movie: movie.add_genre(genre)
                except (ValueError, IndexError):
                    continue
