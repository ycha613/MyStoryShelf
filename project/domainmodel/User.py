from __future__ import annotations

def validate_username(username: str) -> bool:
    if not isinstance(username, str):
        raise TypeError("Username must be a string.")
    
    if len(username.strip()) < 3:
        raise ValueError("Username must be at least 3 characters long.")

def validate_password(password: str) -> bool:
    if not isinstance(password, str):
        raise TypeError("Password must be a string.")
    
    if len(password.strip()) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    has_uppercase = has_lowercase = has_digit = False

    for c in password:
        if c.isupper(): has_uppercase = True
        if c.islower(): has_lowercase = True
        if c.isdigit(): has_digit = True
    if (has_uppercase == False or has_lowercase == False or has_digit == False):
        raise ValueError("Password must have at least one uppercase, one lowercase and one digit.")


class User:
    def __init__(self, username: str, password: str):
        validate_username(username)
        self._username = username
        validate_password(password)
        self._password = password
        
    @property
    def username(self) -> str:
        return self._username
    
    @property
    def password(self) -> str:
        return self._password
    
    def __repr__(self):
        return f"<User: {self.username}>"
    
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.username == other.username
    
    def __lt__(self, other):
        if not isinstance(other, User):
            return False
        return self.username < other.username
    
    def __hash__(self):
        return hash(self.username)