from django.shortcuts import render

# Create your views here.

# A função render do Django é responsável por ler e renderizar um arquivo web
# Sem ela, teríamos que escrever código web dentro das funções das views

# Outro ponto muito importante do Django é o uso de namespace
# namespace em resumo é uma metodologia empregada na hora de nomear
# rotas (URLs) e templates, sempre utilizando um diretório que se 
# refere ao app, no recurso de template ex: receitas/templates/receitas/index.html

def pag_inicial(request):
    return render(request, 'receitas/pag_inicial.html')

def pag_contato(request):
    return render(request, 'receitas/pag_contatos.html')
