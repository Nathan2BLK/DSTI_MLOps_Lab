import pytest
from Unit_testing import is_valid_username, is_valid_password, is_valid_email, register_user

# Tests for username validation
def test_is_valid_username():
    assert is_valid_username("user123") is True
    assert is_valid_username("") is False
    assert is_valid_username("user name") is False

# Tests for password validation
def test_is_valid_password():
    assert is_valid_password("P@ssw0rd") is True
    assert is_valid_password("password") is False  # No number or special character
    assert is_valid_password("12345678") is False  # No letter or special character
    assert is_valid_password("P@ss") is False      # Too short

# Tests for email validation
def test_is_valid_email():
    assert is_valid_email("user@example.com") is True
    assert is_valid_email("userexample.com") is False
    assert is_valid_email("user@com") is False
    assert is_valid_email("user@.com") is False

# Tests for full registration
def test_register_user():
    assert register_user("user123", "user@example.com", "P@ssw0rd") == {
        "username": "user123",
        "email": "user@example.com",
        "password": "P@ssw0rd"
    }

    with pytest.raises(ValueError, match="Invalid username"):
        register_user("", "user@example.com", "P@ssw0rd")

    with pytest.raises(ValueError, match="Invalid email"):
        register_user("user123", "userexample.com", "P@ssw0rd")

    with pytest.raises(ValueError, match="Invalid password"):
        register_user("user123", "user@example.com", "password")