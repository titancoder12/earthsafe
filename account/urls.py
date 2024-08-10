from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("viewaccount/<int:id>", views.index, name="viewaccount"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]