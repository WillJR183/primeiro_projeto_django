from django.urls import path
from receitas.views import pag_inicial, pag_contato

# Rotas

urlpatterns = [
    path('', pag_inicial),  # dominio + '/'
    path('contato/', pag_contato),  # dominio + '/contato'
]
