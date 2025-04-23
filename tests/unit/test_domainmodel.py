import pytest
from project.domainmodel.User import User

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


# Movie class unit tests


# Show class unit tests