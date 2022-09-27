from django.shortcuts import render

# Create your views here.

def pag_inicial(request):
    return render(request, 'receitas/pag_inicial.html', context = {
        'name':'Willian JR.'
    })
