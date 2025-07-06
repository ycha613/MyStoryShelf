from werkzeug.security import generate_password_hash, check_password_hash
from project.adapters.repository import AbstractRepository
from project.domainmodel.User import User

class NameNotUniqueException(Exception):
    pass

class UnknownUserException(Exception):
    pass

class AuthenticationException(Exception):
    pass


def add_user(user_name: str, password: str, repo: AbstractRepository):
    user = repo.get_user(user_name)
    if user is not None:
        raise NameNotUniqueException
    
    password_hash = generate_password_hash(password)
    new_user = User(user_name, password_hash)
    repo.add_user(new_user)


def get_user_dict(user_name: str, repo: AbstractRepository):
    user = repo.get_user(user_name)
    if user is None:
        raise UnknownUserException
    
    return user_to_dict(user)


def authenticate_user(user_name: str, password: str, repo: AbstractRepository):
    authenticated = False
    user = repo.get_user(user_name)
    if user is not None:
        authenticated = check_password_hash(user.password, password)
    if not authenticated:
        raise AuthenticationException


def user_to_dict(user: User):
    user_dict = {
        'user_name': user.username,
        'password' : user.password
    }
    return user_dict


def get_user(username: str, repo: AbstractRepository) -> User:
    return repo.get_user(username)