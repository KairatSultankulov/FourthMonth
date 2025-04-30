from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmListView.as_view(), name='films'),
    path('film_list/<int:id>/', views.film_detail),
    path('emodji/', views.emodji),
    path('text/', views.text),
    path('image/', views.image),
    path('search/', views.SearchFilmView.as_view(), name='search'),
]

