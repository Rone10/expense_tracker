import pytest
from django.contrib.auth import get_user_model

from users.forms import CustomLoginForm, UserCreateForm

User = get_user_model()


@pytest.mark.django_db
class TestUserForms:
    def test_login_form(self):
        form = CustomLoginForm(data={})
        assert form.is_valid() is False
        get_user_model().objects.create_user(
            username="mawdorone", password="waynerooney10"
        )
        form = CustomLoginForm(
            data={"username": "mawdorone", "password": "waynerooney10"}
        )

        assert form.is_valid() is True

    def test_signup_form(self):
        form = UserCreateForm(data={})
        assert form.is_valid() is False

        form = UserCreateForm(
            data={
                "first_name": "testuser",
                "last_name": "testpass",
                "email": "test@email.com",
                "username": "testuser",
                "password1": "raymondreddington",
                "password2": "raymondreddington",
            }
        )
        assert form.is_valid() is True
