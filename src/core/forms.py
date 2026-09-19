from typing import Any

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ("username", "password")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Usuario"
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Tu usuario", "autocomplete": "username"}
        )
        self.fields["password"].label = "Contraseña"
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Tu contraseña", "autocomplete": "current-password"}
        )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        field_attrs = {
            "username": {
                "class": "form-control",
                "placeholder": "Elige un usuario",
                "autocomplete": "username",
            },
            "password1": {
                "class": "form-control",
                "placeholder": "Crea una contraseña",
                "autocomplete": "new-password",
            },
            "password2": {
                "class": "form-control",
                "placeholder": "Repite la contraseña",
                "autocomplete": "new-password",
            },
        }
        for name, attrs in field_attrs.items():
            self.fields[name].widget.attrs.update(attrs)
            self.fields[name].help_text = ""
