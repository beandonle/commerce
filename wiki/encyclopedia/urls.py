from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:label>/", views.title, name="title"),    # views.title: goes to title function in views.py. <str:title> is passed as paramter to title function
    path("wiki/newpage", views.newPage, name="newPage"),
    path("wiki/randpage", views.randPage, name="randPage"),
    path("wiki/s", views.search, name="search"),
    path("wiki/s/<str:label>/", views.title, name="searchResult"),
    path("wiki/edit/<str:label>/", views.edit, name="edit")
    
    
]
