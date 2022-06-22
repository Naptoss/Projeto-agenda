from django.shortcuts import render, get_list_or_404
from .models import Contato
from django.http import Http404

def index(request):
    contatos = Contato.objects.all() # aqui esta selecionando todos os itens da base de dados
    return render(request,'contatos/index.html',{
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    contato = get_list_or_404(Contato,id=contato_id) # aqui ele verifica se o id ta registrado, se nao tiver ele retorna o erro 404 
    return render(request,'contatos/ver_contato.html',{
            'contato': contato
    }) 
   