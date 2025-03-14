from django.urls import path
from . import views

urlpatterns = [
    path('all_hashtags_films/', views.all_category_film, name='all'),
    path('comedy_hashtags_films/', views.comedy_category_film, name='comedy'),
    path('comics_hashtags_films/', views.comics_category_film, name='comics'),
]