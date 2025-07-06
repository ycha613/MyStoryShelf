from sqlalchemy import Table, Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import registry, relationship
from project.domainmodel.Movie import Movie, Genre
from project.domainmodel.User import User

mapper_registry = registry()


movies_table = Table(
    'movies', mapper_registry.metadata,
    Column('movie_id', Integer, primary_key=True),
    Column('title', String(255), nullable=False),
    Column('poster_link', Text),
    Column('description', Text),
    Column('release_year', Integer),
    Column('runtime', Integer)
)

genres_table = Table(
    'genres', mapper_registry.metadata,
    Column('genre_id', Integer, primary_key=True),
    Column('name', String(255), nullable=False)
)

movie_genres_table = Table(
    'movie_genres', mapper_registry.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('movie_id', Integer, ForeignKey('movies.movie_id')),
    Column('genre_id', Integer, ForeignKey('genres.genre_id'))
)

users_table = Table(
    'users', mapper_registry.metadata,
    Column('user_id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False)
)


def map_model_to_tables():
    mapper_registry.map_imperatively(Movie, movies_table, properties={
        '_id': movies_table.c.movie_id,
        '_title': movies_table.c.title,
        '_poster_link': movies_table.c.poster_link,
        '_description': movies_table.c.description,
        '_release_year': movies_table.c.release_year,
        '_runtime': movies_table.c.runtime,
        '_genres': relationship(Genre, secondary=movie_genres_table)
    })

    mapper_registry.map_imperatively(Genre, genres_table, properties={
        '_id': genres_table.c.genre_id,
        '_name': genres_table.c.name
    })

    mapper_registry.map_imperatively(User, users_table, properties={
        '_id': users_table.c.user_id,
        '_username': users_table.c.username,
        '_password': users_table.c.password
    })