import pytest
from project.domainmodel import User

@pytest.fixture
def my_user():
    return User("john", "Password123")