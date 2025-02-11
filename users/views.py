from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginForm, RegisterForm


class MyLoginView(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm
    next_page = '/'


class MyLogoutView(LogoutView):
    template_name = "users/logout.html"


class MyRegisterView(CreateView):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("user:login")
