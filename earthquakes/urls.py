from django.urls import path
from . import views

urlpatterns = [
    path("earthquakeendpoint", views.index, name="index"),
]