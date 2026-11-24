import pytest
from app.schemas.user import UserRegister
from pydantic import ValidationError


def test_email_is_lowercase():
    user = UserRegister(email="TEST@GMAIL.COM", password="12345678")

    assert user.email == "test@gmail.com"


def test_password_is_invalid():
    with pytest.raises(ValidationError):
        UserRegister(email="test@gmail.com", password="123")

    with pytest.raises(ValidationError):
        UserRegister(email="test@gmail.com", password="        ")

    with pytest.raises(ValidationError):
        UserRegister(email="test@gmail.com", password="a" * 129)


def test_password_is_valid():
    user = UserRegister(email="test@gmail.com", password="my secure password")

    assert user.password == "my secure password"
