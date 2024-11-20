import re

def is_valid_username(username):
    """Validate username: must not be empty and contain no spaces."""
    return bool(username) and ' ' not in username

def is_valid_password(password):
    """Validate password: must meet length, character, and complexity requirements."""
    if len(password) < 8:
        return False
    if not re.search(r'[A-Za-z]', password):  # At least one letter
        return False
    if not re.search(r'\d', password):  # At least one digit
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # At least one special character
        return False
    return True

def is_valid_email(email):
    """Validate email: must contain '@' and '.'."""
    return '@' in email and '.' in email

def get_user_input():
    """Prompt the user for registration details."""
    username = input("Enter username: ").strip()
    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()
    return username, email, password

def register_user(username, email, password):
    """Validate user input and register if valid."""
    if not is_valid_username(username):
        raise ValueError("Invalid username: it must not be empty and cannot contain spaces.")
    if not is_valid_email(email):
        raise ValueError("Invalid email: it must contain '@' and '.'.")
    if not is_valid_password(password):
        raise ValueError("Invalid password: it must be at least 8 characters long, "
                         "contain a letter, a number, and a special character.")
    return {"username": username, "email": email, "password": password}

