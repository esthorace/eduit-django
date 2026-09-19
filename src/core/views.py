from datetime import UTC, datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_not_required  # type:ignore

# from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.forms import LoginForm, RegisterForm


@login_not_required
def index(request):

    año_actual = datetime.now(UTC).year
    contexto = {"año": año_actual, "autor": "EduIT"}
    return render(request, "core/index.html", contexto)


class CustomLoginView(LoginView):
    template_name = "core/login.html"
    authentication_form = LoginForm
    next_page = "core:home"

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        messages.success(self.request, f"Inicio de sesión exitoso\n ¡Bienvenido {form.get_user()}!")
        return super().form_valid(form)


# class CustomRegisterView(LoginRequiredMixin, CreateView):
class CustomRegisterView(CreateView):
    form_class = RegisterForm
    template_name = "core/register.html"
    success_url = reverse_lazy("core:login")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, "Registro exitoso. Puedes iniciar sesión")
        return super().form_valid(form)
