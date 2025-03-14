from django.urls import path
from .views import fake_login

urlpatterns = [
    path("login/", fake_login, name="fake_login"),
]