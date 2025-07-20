import pytest
from project.domainmodel.User import User, MovieNote
from project.domainmodel.Movie import Movie, Genre
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from project.adapters.orm import mapper_registry, map_model_to_tables
from project.adapters.database_repository import DatabaseRepository, database_repository_populate
from project.adapters.csv_reader import MovieCSVReader

TEST_MOVIES_FULL = 'project/adapters/data/movies/movies.csv'
TEST_GENRES_FULL = 'project/adapters/data/movies/genres.csv'
TEST_POSTERS_FULL = 'project/adapters/data/movies/posters.csv'
TEST_MOVIES_LIMITED = 'project/adapters/data/movies/movies.csv'
TEST_GENRES_LIMITED = 'project/adapters/data/movies/genres.csv'
TEST_POSTERS_LIMITED = 'project/adapters/data/movies/posters.csv'

TEST_DATABASE_URI_IN_MEMORY = 'sqlite://'
TEST_DATABASE_URI_FILE = 'sqlite:///podcasts-test.db'

# Domain Model Fixtures
@pytest.fixture
def my_user():
    return User(username="john", password="Password123")

@pytest.fixture
def my_movie():
    return Movie(id=10101, title="Psycho", release_year=1960)

@pytest.fixture
def my_genre():
    return Genre(id=1, name="Action")

@pytest.fixture
def my_movienote(my_movie, my_user):
    return MovieNote(movie=my_movie, user=my_user, note="test")


#  Database Fixtures
@pytest.fixture
def database_engine():
    clear_mappers()
    engine = create_engine(TEST_DATABASE_URI_FILE)
    mapper_registry.metadata.create_all(engine)
    for table in reversed(mapper_registry.metadata.sorted_tables):
        with engine.connect() as connection:
            connection.execute(table.delete())
    map_model_to_tables()
    csv_reader = MovieCSVReader(movies_file=TEST_MOVIES_LIMITED, genres_file=TEST_GENRES_LIMITED,
                                posters_file=TEST_POSTERS_LIMITED)
    session_factory = sessionmaker(autocommit=False, autoflush=True, bind=engine)
    repo_instance = DatabaseRepository(session_factory)
    database_repository_populate(csv_reader, repo_instance)
    yield engine
    mapper_registry.metadata.drop_all(engine)

@pytest.fixture
def session_factory():
    clear_mappers()
    engine = create_engine(TEST_DATABASE_URI_IN_MEMORY)
    mapper_registry.metadata.create_all(engine)
    for table in reversed(mapper_registry.metadata.sorted_tables):
        with engine.connect() as connection:
            connection.execute(table.delete())
    map_model_to_tables()
    csv_reader = MovieCSVReader(movies_file=TEST_MOVIES_LIMITED, genres_file=TEST_GENRES_LIMITED,
                                posters_file=TEST_POSTERS_LIMITED)
    session_factory = sessionmaker(autocommit=False, autoflush=True, bind=engine)
    repo_instance = DatabaseRepository(session_factory)
    database_repository_populate(csv_reader, repo_instance)
    yield session_factory
    mapper_registry.metadata.drop_all(engine)

@pytest.fixture
def empty_session():
    clear_mappers()
    engine = create_engine(TEST_DATABASE_URI_IN_MEMORY)
    mapper_registry.metadata.create_all(engine)
    for table in reversed(mapper_registry.metadata.sorted_tables):
        with engine.connect() as connection:
            connection.execute(table.delete())
    map_model_to_tables()
    session_factory = sessionmaker(bind=engine)
    yield session_factory()
    mapper_registry.metadata.drop_all(engine)