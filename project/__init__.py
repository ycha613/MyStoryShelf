"""
Initialize the flask app
"""

from flask import Flask
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.pool import NullPool
import os

import project.adapters.repository as repo
from project.adapters.database_repository import DatabaseRepository, database_repository_populate
from project.adapters.csv_reader import MovieCSVReader
from project.adapters.orm import map_model_to_tables, mapper_registry

movies_filename = 'project/adapters/data/movies/movies.csv'
genres_filename = 'project/adapters/data/movies/genres.csv'
posters_filename = 'project/adapters/data/movies/posters.csv'

def create_app():
    app = Flask(
        __name__, 
        template_folder=os.path.join(os.path.dirname(__file__), "templates")
    )
    app.config.from_object('config.Config')


    # link database to repo
    database_uri = app.config["SQLALCHEMY_DATABASE_URI"]
    database_echo = app.config["SQLALCHEMY_ECHO"]
    database_engine = create_engine(database_uri, connect_args={"check_same_thread": False},
                                        poolclass=NullPool, echo=database_echo)
    session_factory = sessionmaker(autocommit=False, autoflush=True, bind=database_engine)
    repo.repo_instance = DatabaseRepository(session_factory)

    # create database if not created, map domain model to tables
    insp = inspect(database_engine)
    if len(insp.get_table_names()) == 0:
        print("Repopulating database...")
        clear_mappers()
        mapper_registry.metadata.create_all(database_engine)
        for table in reversed(mapper_registry.metadata.sorted_tables):
            with database_engine.connect() as connection:
                connection.execute(table.delete())
        map_model_to_tables()
        csv_reader = MovieCSVReader(movies_file=movies_filename, genres_file=genres_filename,
                                posters_file=posters_filename)
        database_repository_populate(csvreader=csv_reader, repo=repo.repo_instance)
        print("Repopulating database... Finished")
    else:
        map_model_to_tables()


    with app.app_context():
        # register blueprints
        from .home import home
        app.register_blueprint(home.home_blueprint)
        from .browse import browse
        app.register_blueprint(browse.browse_blueprint)

        # register callbacks to ensure database sessions are correct
        @app.before_request
        def before_flask_http_request_function():
            if isinstance(repo.repo_instance, DatabaseRepository):
                repo.repo_instance.reset_session()

        @app.teardown_appcontext
        def shutdown_session(exception=None):
            if isinstance(repo.repo_instance, DatabaseRepository):
                repo.repo_instance.reset_session()

    return app