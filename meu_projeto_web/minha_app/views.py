
# Create your views here.
# minha_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home_view(request):
    """
    Renderiza a página inicial com um template HTML, passando a data e hora atuais como contexto.
    """
    context = {
        'data_e_hora': datetime.now() # Variável Python que será acessível no template HTML
    }
    return render(request, 'meu_primeiro_html.html', context) # Renderiza o template especificado

def login(request):
    nome='Lucas'
    if nome == 'Deby':
        resposta = 'Acesso liberado'
    else:
        resposta = 'Acesso negado'
    return HttpResponse