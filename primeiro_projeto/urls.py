"""primeiro_projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Funcionamento: HTTP Request (cliente solicita) <-> HTTP Response (servidor responde)

# HTTP Request
def minha_view(request): # função que recebe um request e retorna um response
    return HttpResponse('Isso é um teste simulando a resposta do servidor para o cliente.')


# Rotas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contato/', minha_view),
]
