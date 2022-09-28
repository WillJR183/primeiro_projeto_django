from django.shortcuts import render

# Create your views here.

def pag_inicial(request):
    return render(request, 'receitas/pages/pag_inicial.html', context = {
        'name':'Willian JR.'
    })
