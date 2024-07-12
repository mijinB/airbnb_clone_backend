from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    # username & password 이용한 login
    path("log-in", views.Login.as_view()),
    path("log-out", views.Logout.as_view()),
    # username & password & auth Token 이용한 login
    path("token-login", obtain_auth_token),
    # username & password 이용한 JWT login
    path("jwt-login", views.JWTLogin.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),
]
