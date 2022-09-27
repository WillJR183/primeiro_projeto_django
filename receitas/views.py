from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pag_inicial(request):
    return HttpResponse('<strong> Página Inicial <strong>')

def pag_contato(request):
    return HttpResponse('<strong> Página de Informações de Contato <strong>')
