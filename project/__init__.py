"""
Initialize the flask app
"""

from flask import Flask
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.pool import NullPool
import os

import project.repositories.repository as repo
from project.repositories.database_repository import DatabaseRepository

def create_app():
    app = Flask(
        __name__, 
        template_folder=os.path.join(os.path.dirname(__file__), "templates")
    )
    app.config.from_object('config.Config')

    # link database to repo
    database_uri = app.config["SQLALCHEMY_DATBASE_URI"]
    database_echo = app.config["SQLALCHEMY_ECHO"]
    database_engine = create_engine(database_uri, connect_arge={"check_same_thread": False},
                                        poolclass=NullPool, echo=database_echo)
    session_factory = sessionmaker(autocommit=False, autoflush=True, bind=database_engine)
    repo.repo_instance = DatabaseRepository()

    # create database if not created
    insp = inspect(database_engine)
    if len(insp.get_table_names()) == 0:
        print("Repopulating database...")
        clear_mappers()
        mapper_registry.metadata.create_all(database_engine) # need to implement mapper_registry
        for table in reversed(mapper_registry.metadata.sorted_tables): # need to implement mapper_registry
            with database_engine.connect() as connection:
                connection.execute(table.delete())
        map_model_to_tables() # need to implement this function
        print("Repopulating database... Finished")
    else:
        map_model_to_tables() # need to implement this function

    with app.app_context():
        # register blueprints
        from .home import home
        app.register_blueprint(home.home_blueprint)

    return app