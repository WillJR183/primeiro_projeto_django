from django.urls import path
from receitas.views import pag_inicial

# Rotas

urlpatterns = [
    path('', pag_inicial),
]
