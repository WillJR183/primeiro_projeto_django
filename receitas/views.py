from django.shortcuts import render

# Create your views here.

# A função render do Django é responsável por ler e renderizar um arquivo web
# Sem ela, teríamos que escrever código web dentro das funções das views

# Outro ponto muito importante do Django é o uso de namespace
# namespace em resumo é uma metodologia empregada na hora de nomear
# rotas (URLs) e templates, sempre utilizando um diretório que se 
# refere ao app, no recurso de template ex: receitas/templates/receitas/index.html

# A função render também possui outros argumentos opcionais, onde podemos por exemplo
# passar variáveis, listas, dicionários pelo context ou até mesmo um status code
# E podemos usar esses dados nas views para exibir o conteúdo por exemplo.  

def pag_inicial(request):
    return render(request, 'receitas/pag_inicial.html')

def pag_contato(request):
    return render(request, 'receitas/pag_contatos.html', context = {
        'name':'Willian JR.'
    }, status = 202)
