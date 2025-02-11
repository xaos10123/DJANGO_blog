from django.urls import path

from users.views import MyLoginView, MyLogoutView, MyRegisterView

app_name = "user"

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("register/", MyRegisterView.as_view(), name="register"),
]
