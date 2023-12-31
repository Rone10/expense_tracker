from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Username", "id": "username"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Enter P",
                "id": "passwordsss",
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = False
        self.fields["password"].label = False


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "id": "first_name",
                "placeholder": "First Name",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "id": "lasts_name",
                "placeholder": "Last Name",
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-input", "placeholder": "Email", "id": "email"}
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-input", "id": "username", "placeholder": "Username"}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Password", "id": "password1"}
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Re-type Password",
                "id": "password2",
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["first_name"].label = False
        self.fields["last_name"].label = False
        self.fields["username"].label = False
        self.fields["email"].label = False
        self.fields["password1"].label = False
        self.fields["password2"].label = False
