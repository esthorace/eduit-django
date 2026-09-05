from datetime import UTC, datetime

from django.contrib.auth.views import LoginView
from django.shortcuts import render

from core.forms import LoginForm


def index(request):

    año_actual = datetime.now(UTC).year
    contexto = {"año": año_actual, "autor": "EduIT"}
    return render(request, "core/index.html", contexto)


class CustomLoginView(LoginView):
    template_name = "core/login.html"
    authentication_form = LoginForm
    next_page = "core:home"
