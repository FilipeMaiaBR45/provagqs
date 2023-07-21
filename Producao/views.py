from django.shortcuts import render, redirect, get_object_or_404

from Producao.forms import ColetaForm
from .models import Criacao
from .models import Coleta
from django.db.models import Sum
from datetime import date, timedelta
from django.db.models.functions import TruncMonth
from django.shortcuts import render, redirect
from .forms import CriacaoForm

def index(request):
   return render(request, "producao/index.html")


def criar_criacao(request):
    if request.method == 'POST':
        form = CriacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producao:listar_criacoes')  # redirecionar para a página de sucesso após criar a Criacao
    else:
        form = CriacaoForm()
    
    return render(request, 'Producao/criar_criacao.html', {'form': form})

def listar_criacoes(request):
    criacoes = Criacao.objects.all()
    return render(request, 'Producao/criacao_list.html', {'criacoes': criacoes})


def listar_coletas(request):
    lista_produtos = Coleta.objects.all()

    informacoes = {
        'lista_produtos': lista_produtos
    }

    return render(request, 'Producao/coleta_list.html', informacoes)

def criar_coleta(request):
    if request.method == 'POST':
        form = ColetaForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('producao:listar_coletas')
    else:
        form = ColetaForm()
    
    return render(request, 'Producao/criar_coleta.html', {'form': form})

def detalhes_coleta(request, pk):
    coleta = Coleta.objects.get(pk=pk)
    informacoes = {
        'coleta': coleta
    }
    return render(request, 'Producao/detalhes_coleta.html', informacoes)

def deletar_coleta(request, pk):
    coleta = Coleta.get_object_or_404(Coleta, pk=pk)
    if request.method == 'POST':
        coleta.delete()
        return redirect('Producao/coleta_list.html')  # Redirecione para a página que lista todas as coletas

    return render(request, 'confirmar_delecao.html', {'coleta': coleta})

def editar_coleta(request, pk):
    coleta = get_object_or_404(Coleta, pk=pk)
    if request.method == 'POST':
        form = ColetaForm(request.POST, instance=coleta)
        if form.is_valid():
            form.save()
            #return redirect('producao:detalhes_coleta', pk=coleta.id)  # Redirecionar para a página de detalhes da coleta
    else:
        form = ColetaForm(instance=coleta)

    return render(request, 'Producao/editar_coleta.html', {'form': form, 'coleta': coleta})

def relatorio_coletas(request):
    today = date.today()
    twelve_months_ago = today - timedelta(days=365)

    coletas = Coleta.objects.filter(data__gte=twelve_months_ago, data__lte=today)

    meses_coletas = coletas.annotate(mes_coleta=TruncMonth('data')).values('mes_coleta').annotate(soma_quantidade=Sum('quantidade'))

    return render(request, 'Producao/relatorio_coletas.html', {'meses_coletas': meses_coletas})