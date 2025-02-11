from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = forms.TextInput(
            attrs={"class": "form-control"}
        )
        self.fields["username"].label = "Логин"
        self.fields["password"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["password"].label = "Пароль"


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = forms.TextInput(
            attrs={"class": "form-control"}
        )
        self.fields["username"].label = "Логин"
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["password1"].label = "Пароль"
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["password2"].label = "Повторите пароль"
