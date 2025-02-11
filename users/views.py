from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from users.forms import LoginForm, ProfileEditForm, ProfilePasswordForm, RegisterForm


class OwnerPermissionMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_owner"] = self.request.user == self.get_object()
        return context


class MyLoginView(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm
    next_page = "main"


class MyLogoutView(LogoutView):
    next_page = "main"


class MyRegisterView(CreateView):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("user:login")


class ProfileDetailView(OwnerPermissionMixin, DetailView):
    model = get_user_model()
    template_name = "users/profile.html"
    context_object_name = "user_prof"


class ProfileEditView(LoginRequiredMixin, OwnerPermissionMixin, UpdateView):
    model = get_user_model()
    template_name = "users/profile_edit.html"
    form_class = ProfileEditForm
    login_url = reverse_lazy("user:login")

    def get_success_url(self):
        return reverse_lazy("user:profile", kwargs={"pk": self.object.pk})


class ProfilePasswordView(LoginRequiredMixin, PasswordChangeView):
    model = get_user_model()
    template_name = "users/profile_change_password.html"
    form_class = ProfilePasswordForm
    login_url = reverse_lazy("user:login")

    def get_success_url(self):
        return reverse_lazy("user:profile", kwargs={"pk": self.request.user.pk})
