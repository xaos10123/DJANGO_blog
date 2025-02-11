from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User


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


class ProfileEditForm(forms.ModelForm):   
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


class ProfilePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["new_password1"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["new_password2"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )
