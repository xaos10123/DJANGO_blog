from django.contrib import messages
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

    def form_valid(self, form):
        messages.success(self.request, f"Добро пожаловать, {form.get_user().username}!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Неверные данные!")
        return super().form_invalid(form)


class MyLogoutView(LogoutView):
    template_name = "logout.html"
    next_page = "main"

    def post(self, request, *args, **kwargs):
        messages.success(request, "Вы вышли из системы!")
        return super().post(request, *args, **kwargs)
    


class MyRegisterView(CreateView):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("user:login")

    def form_valid(self, form):
        messages.success(self.request, "Вы успешно зарегистрировались!")
        return super().form_valid(form)


class ProfileDetailView(OwnerPermissionMixin, DetailView):
    model = get_user_model()
    template_name = "users/profile.html"
    context_object_name = "user_prof"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user != self.get_object():
            messages.error(self.request, "Страница доступна только для просмотра!")
        return context


class ProfileEditView(LoginRequiredMixin, OwnerPermissionMixin, UpdateView):
    model = get_user_model()
    template_name = "users/profile_edit.html"
    form_class = ProfileEditForm
    context_object_name = "user_prof"
    login_url = reverse_lazy("user:login")

    def form_valid(self, form):
        messages.success(self.request, "Данные успешно изменены!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Неверные данные")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("user:profile", kwargs={"pk": self.object.pk})


class ProfilePasswordView(LoginRequiredMixin, PasswordChangeView):
    model = get_user_model()
    template_name = "users/profile_change_password.html"
    form_class = ProfilePasswordForm
    login_url = reverse_lazy("user:login")

    def form_valid(self, form):
        messages.success(self.request, "Пароль успешно изменен!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("user:profile", kwargs={"pk": self.request.user.pk})
