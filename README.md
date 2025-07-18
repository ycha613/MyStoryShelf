# MyStoryShelf
MyStoryShelf is flask web app that allows a user to track and review all sorts of media including movies, shows and books. Keep track of what you have watched and read, what you want to watch and read, and also what you are currently watching and reading while also making personal notes.

## Installation

**Installation via requirements.txt**

**Windows**
```shell
$ cd <project directory>
$ python3 -m venv .venv
$ .venv\Scripts\activate
$ pip install -r requirements.txt
```

**MacOS**
```shell
$ cd <project directory>
$ python3 -m venv .venv
$ source .venv/Scripts/activate
$ pip install -r requirements.txt
```

## Execution

**Running the application**
From the *project directory* and within the activated virtual environment:
````shell
$ flask run
````

## Testing
To run the tests in the 'tests' folder:
```shell
$ python -m pytest -v tests
```

## Configuration

The *project directory/.env* file contains variable settings. They are set with appropriate values.

* `FLASK_APP`: Entry point of the application (should always be `wsgi.py`).
* `FLASK_ENV`: The environment in which to run the application (either `development` or `production`).
* `SECRET_KEY`: Secret key used to encrypt session data.
* `TESTING`: Set to False for running the application. Overridden and set to True automatically when testing the application.
* `WTF_CSRF_SECRET_KEY`: Secret key used by the WTForm library.
* `SQLALCHEMY_DATABASE_URI`: Database URI for connection ("sqlite:///storyshelf.db" for sqlite) or ("mysql+pymysql://root:password@localhost/mystoryshelf" for MySQL), default is sqlite so you do not have to set up MySQL on your machine if not already installed.

## Data sources

The data files are downloaded from: 

https://www.kaggle.com/datasets/gsimonx37/letterboxd?select=movies.csv

Used movies.csv, posters.csv and genres.csv

