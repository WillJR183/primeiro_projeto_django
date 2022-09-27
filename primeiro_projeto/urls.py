from django.contrib import admin
from django.urls import path, include

# Rotas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('receitas.urls'))
]
