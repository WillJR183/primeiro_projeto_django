from django.urls import path
from . import views

# Rotas

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe)
]
