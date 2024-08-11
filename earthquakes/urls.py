from django.urls import path
from . import views

app_name = 'earthquakes'
urlpatterns = [
    path("", views.earthquakes, name="earthquakes"),
    path("addstatus", views.addstatus, name="addstatus"),
    path("earthquake/<int:id>", views.earthquake, name="earthquake")
]