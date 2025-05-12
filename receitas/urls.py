from django.urls import path, include
from receitas.views import contato, home, sobre


urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre)
]