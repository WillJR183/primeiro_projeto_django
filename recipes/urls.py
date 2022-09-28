from django.urls import path
from recipes.views import home

# Rotas

urlpatterns = [
    path('', home),
]
