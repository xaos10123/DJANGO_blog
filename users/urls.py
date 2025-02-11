from django.urls import path

from users.views import (
    MyLoginView,
    MyLogoutView,
    MyRegisterView,
    ProfileDetailView,
    ProfileEditView,
    ProfilePasswordView,
)

app_name = "user"

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("register/", MyRegisterView.as_view(), name="register"),
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name="profile"),
    path("profile/<int:pk>/edit/", ProfileEditView.as_view(), name="profile_edit"),
    path(
        "profile/<int:pk>/password/",
        ProfilePasswordView.as_view(),
        name="profile_password",
    ),
]
