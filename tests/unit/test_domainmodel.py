import pytest
from project.domainmodel.User import User
from project.domainmodel.Media import Book, Movie, Show

"""
Unit tests for the domain model of the web application
"""

# User class unit tests

def test_user_initialisation():
    user1 = User("john", "Password1")
    assert repr(user1) == "<User: john>"
    assert user1.username == "john"
    assert user1.password == "Password1"

    with pytest.raises(TypeError):
        user2 = User(1, "Password1")
    with pytest.raises(TypeError):
        user2 = User("john", 1)

    with pytest.raises(ValueError):
        user2 = User("", "Password1")
    with pytest.raises(ValueError):
        user2 = User("john", "")

def test_user_eq():
    user1 = User("aaron", "Password1")
    user2 = User("aaron", "Password2")
    user3 = User("chris", "Password3")
    assert user1 == user2
    assert user1 != user3
    assert user3 == user3

def test_user_lt():
    user1 = User("aaron", "Password1")
    user2 = User("brian", "Password2")
    user3 = User("chris", "Password3")
    assert user1 < user2 < user3
    user_list = [user3, user2, user1]
    assert sorted(user_list) == [user1, user2, user3]

def test_user_hash():
    user1 = User("aaron", "Password1")
    user2 = User("brian", "Password2")
    user3 = User("chris", "Password3")
    user_set = set()
    user_set.add(user1)
    user_set.add(user2)
    user_set.add(user3)
    
    assert len(user_set) == 3
    assert repr(sorted(user_set)) == "[<User: aaron>, <User: brian>, <User: chris>]"
    user_set.discard(user1)
    assert repr(sorted(user_set)) == "[<User: brian>, <User: chris>]"


# Book class unit tests

def test_book_initialisation(my_user):
    book1 = Book(title="Moby Dick", user=my_user, author="Herman Melville")
    assert repr(book1) == "<Book: Moby Dick>"
    assert book1.title == "Moby Dick"
    assert book1.author == "Herman Melville"

    with pytest.raises(TypeError):
        book2 = Book(title=3, user=my_user, author="Herman Melville")
    with pytest.raises(TypeError):
        book2 = Book(title="Moby Dick 2", user=2, author="Herman Melville")
    with pytest.raises(TypeError):
        book2 = Book(title="Moby Dick 2", user=my_user, author=2)

    with pytest.raises(ValueError):
        book2 = Book(title="", user=my_user, author="Herman Melville")
    with pytest.raises(ValueError):
        book2 = Book(title="Moby Dick 2", user=my_user, author="")

    book2 = Book(title="moby DICK", user=my_user, author="herman MELVILLE")
    assert book2.title == "Moby Dick"
    assert book2.author == "Herman Melville"

def test_book_eq(my_user):
    book1 = Book(title="Moby Dick", user=my_user, author="Herman Melville")
    book2 = Book(title="Moby Dick", user=my_user, author="Herman Melville")
    book3 = Book(title="Neverland", user=my_user, author="Herman Melville")
    book4 = Book(title="Moby Dick", user=my_user, author="John Richards")
    assert book1 == book2
    assert book1 != book3
    assert book1 != book4
    assert book4 == book4

def test_book_lt(my_user):
    book1 = Book(title="Moby Dick", user=my_user, author="Herman Melville")
    book2 = Book(title="Neverland", user=my_user, author="Herman Melville")
    book3 = Book(title="Orpheus", user=my_user, author="Herman Melville")
    books_list = [book3, book2, book1]
    assert book1 < book2 < book3
    assert sorted(books_list) == [book1, book2, book3]


def test_book_hash(my_user):
    book1 = Book(title="Moby Dick", user=my_user, author="Herman Melville")
    book2 = Book(title="Neverland", user=my_user, author="Herman Melville")
    book3 = Book(title="Orpheus", user=my_user, author="Herman Melville")
    books_set = set()
    books_set.add(book1)
    books_set.add(book2)
    books_set.add(book3)

    assert len(books_set) == 3
    assert repr(sorted(books_set)) == "[<Book: Moby Dick>, <Book: Neverland>, <Book: Orpheus>]"
    books_set.discard(book1)
    assert repr(sorted(books_set)) == "[<Book: Neverland>, <Book: Orpheus>]"


# Movie class unit tests

def test_movie_initialisation(my_user):
    movie1 = Movie(title="Psycho", user=my_user, director="Alfred Hitchcock")
    assert repr(movie1) == "<Movie: Psycho>"
    assert movie1.title == "Psycho"
    assert movie1.director == "Alfred Hitchcock"

    with pytest.raises(TypeError):
        movie2 = Movie(title=3, user=my_user, director="Alfred Hitchcock")
    with pytest.raises(TypeError):
        movie2 = Movie(title="Psycho 2", user=2, director="Alfred Hitchcock")
    with pytest.raises(TypeError):
        movie2 = Movie(title="Psycho 2", user=my_user, director=2)

    with pytest.raises(ValueError):
        movie2 = Movie(title="", user=my_user, director="Alfred Hitchcock")
    with pytest.raises(ValueError):
        movie2 = Movie(title="Psycho 2", user=my_user, director="")

    movie2 = Movie(title="pSycHO", user=my_user, director="alfred HITCHCOCK")
    assert movie2.title == "Psycho"
    assert movie2.director == "Alfred Hitchcock"

def test_movie_eq(my_user):
    movie1 = Movie(title="Psycho", user=my_user, director="Alfred Hitchcock")
    movie2 = Movie(title="Psycho", user=my_user, director="Alfred Hitchcock")
    movie3 = Movie(title="Vertigo", user=my_user, director="Alfred Hitchcock")
    movie4 = Movie(title="Psycho", user=my_user, director="John Richards")
    assert movie1 == movie2
    assert movie1 != movie3
    assert movie1 != movie4
    assert movie4 == movie4

def test_movie_lt(my_user):
    movie1 = Movie(title="Psycho", user=my_user, director="Alfred Hitchcock")
    movie2 = Movie(title="Stage Fright", user=my_user, director="Alfred Hitchcock")
    movie3 = Movie(title="Vertigo", user=my_user, director="Alfred Hitchcock")
    movies_list = [movie3, movie2, movie1]
    assert movie1 < movie2 < movie3
    assert sorted(movies_list) == [movie1, movie2, movie3]


def test_movie_hash(my_user):
    movie1 = Movie(title="Psycho", user=my_user, director="Alfred Hitchcock")
    movie2 = Movie(title="Stage Fright", user=my_user, director="Alfred Hitchcock")
    movie3 = Movie(title="Vertigo", user=my_user, director="Alfred Hitchcock")
    movies_set = set()
    movies_set.add(movie1)
    movies_set.add(movie2)
    movies_set.add(movie3)

    assert len(movies_set) == 3
    assert repr(sorted(movies_set)) == "[<Movie: Psycho>, <Movie: Stage Fright>, <Movie: Vertigo>]"
    movies_set.discard(movie1)
    assert repr(sorted(movies_set)) == "[<Movie: Stage Fright>, <Movie: Vertigo>]"


# Show class unit tests

def test_show_initialisation(my_user):
    show1 = Show(title="Breaking Bad", user=my_user, season=1)
    assert repr(show1) == "<Show: Breaking Bad>"
    assert show1.title == "Breaking Bad"
    assert show1.season == 1

    with pytest.raises(TypeError):
        show2 = Show(title=3, user=my_user, season=1)
    with pytest.raises(TypeError):
        show2 = Show(title="Breaking Bad", user=2, season=1)
    with pytest.raises(TypeError):
        show2 = Show(title="Breaking Bad", user=my_user, season="")

    with pytest.raises(ValueError):
        show2 = Show(title="", user=my_user, season=1)
    with pytest.raises(ValueError):
        show2 = Show(title="Breaking Bad", user=my_user, season=0)

    show2 = Show(title="breaking BAD", user=my_user, season=1)
    assert show2.title == "Breaking Bad"

def test_show_eq(my_user):
    show1 = Show(title="Breaking Bad", user=my_user, season=1)
    show2 = Show(title="Breaking Bad", user=my_user, season=1)
    show3 = Show(title="Breaking Bad", user=my_user, season=2)
    show4 = Show(title="Game Of Thrones", user=my_user, season=1)
    assert show1 == show2
    assert show1 != show3
    assert show1 != show4
    assert show4 == show4

def test_show_lt(my_user):
    show1 = Show(title="Breaking Bad", user=my_user, season=1)
    show2 = Show(title="Breaking Bad", user=my_user, season=2)
    show3 = Show(title="Game Of Thrones", user=my_user, season=1)
    shows_list = [show2, show3, show1]
    assert show1 < show2 < show3
    assert sorted(shows_list) == [show1, show2, show3]


def test_show_hash(my_user):
    show1 = Show(title="Breaking Bad", user=my_user, season=1)
    show2 = Show(title="Breaking Bad", user=my_user, season=2)
    show3 = Show(title="Game Of Thrones", user=my_user, season=1)
    shows_set = set()
    shows_set.add(show1)
    shows_set.add(show2)
    shows_set.add(show3)

    assert len(shows_set) == 3
    assert repr(sorted(shows_set)) == "[<Show: Breaking Bad>, <Show: Breaking Bad>, <Show: Game Of Thrones>]"
    shows_set.discard(show1)
    assert repr(sorted(shows_set)) == "[<Show: Breaking Bad>, <Show: Game Of Thrones>]"