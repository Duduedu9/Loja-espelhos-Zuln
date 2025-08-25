from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Espelho

class ListaEspelhosView(ListView):
    model = Espelho
    template_name = 'loja/lista_espelhos.html'
    context_object_name = 'espelhos' # Nome da variável que será usada no template
   

class DetalheEspelhoView(DetailView):
    model = Espelho
    template_name = 'loja/detalhe_espelho.html'
    context_object_name = 'espelho' # Nome da variável que será usada no template
