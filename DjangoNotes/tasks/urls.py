from django.urls import path
from . import views

app_name = "tasks"      # defines the name of the app to identify specific features within app
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
]