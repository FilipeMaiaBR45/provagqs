from django.shortcuts import render, redirect
from .models import Criacao
from .models import Coleta


def index(request):
   return render(request, "producao/index.html")


def criacoes(request):
    nova_criacao = Criacao()
    nova_criacao.raca = request.POST.get("raca")
    nova_criacao.data_criacao = request.POST.get("data_criacao")
    nova_criacao.save()
    criacoes = {"criacoes": Criacao.objects.all()}
    return render(request, "templates/Producao/criar_producao.html", criacoes)


def salva_coleta(request):
    nova_coleta = Coleta()
    criacao = request.POST.get("criacao")
    nova_coleta.data = request.POST.get("data")
    nova_coleta.quantidade = request.POST.get("quantidade")
    nova_coleta.criacao = Criacao.objects.get(raca=criacao)
    nova_coleta.save()
    coletas = {"coletas": Coleta.objects.all()}
    return render(request, "html/coleta.html", coletas)