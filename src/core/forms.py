from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ("username", "password")

    # username = forms.CharField(
    #     label="Usuario",
    #     widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Usuario"}),
    # )
    # password = forms.CharField(
    #     label="Contraseña",
    #     widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Contraseña"}),
    # )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].help_text = ""
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""
