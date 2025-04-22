import pytest
from project.domainmodel.User import User

"""
Unit tests for the domain model of the web application
"""

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

