import pytest 
from users.forms import CustomLoginForm, UserCreateForm
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from users.views import UserLoginView, UserSignUpView

pytestmark = pytest.mark.django_db

class TestUserViews:
    def test_login_view(self, client):
        url = reverse("users:login")
        response = client.get(url)
        assert response.status_code == 200

    def test_login_view_with_valid_data(self, client):
        user = get_user_model().objects.create_user(username="test", password="test")
        url = reverse("users:login")
        data = {"username": "test", "password": "test"}
        response = client.post(url, data)
        assert response.status_code == 302
        assert response.url == reverse("expenses:expenses")

    def test_login_view_with_invalid_data(self, client):
        url = reverse("users:login")
        data = {"username": "test", "password": "test"}
        response = client.post(url, data)
        assert response.status_code == 200

    def test_login_view_with_authenticated_user(self, client):
        user = get_user_model().objects.create_user(username="test", password="raymondreddington")
        client.force_login(user)
        url = reverse("users:login")
        response = client.get(url)
        assert response.status_code == 302
        assert response.url == reverse("expenses:expenses")

    def test_signup_view(self, client):
        url = reverse("users:signup")
        response = client.get(url)
        assert response.status_code == 200

    def test_signup_view_with_valid_data(self, client):
        url = reverse("users:signup")
        data = {
            "first_name": "testuser",
            "last_name": "testpass",
            "email": "test@email.com",
            "username": "testuser",
            "password1": "raymondreddington",
            "password2": "raymondreddington",
        }
        response = client.post(url, data)
        assert response.status_code == 302
        assert response.url == reverse("users:login")
