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


# Show class unit tests