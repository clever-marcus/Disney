from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tvshow/', views.tvshow, name="tvshow"),
    path('movies/', views.movies, name="movies"),
]