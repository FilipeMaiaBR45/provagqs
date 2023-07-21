

from django.forms import ModelForm, ValidationError
from Producao.models import Coleta, Criacao

class ColetaForm(ModelForm):
    class Meta:
        model = Coleta
        fields = ['criacao', 'data', 'quantidade']

    def clean(self):
        cleaned_data = super().clean()

        criacao = self.cleaned_data['criacao']
        data = self.cleaned_data['data']
        quantidade = self.cleaned_data['quantidade']

        coletas_existentes = Coleta.objects.filter(criacao=criacao, data=data, quantidade=quantidade)

        if len(coletas_existentes) > 0:
            raise ValidationError("Já existe uma coleta cadastrada para esta criação nesta data.")

class CriacaoForm(ModelForm):
    class Meta:
        model = Criacao
        fields = ['raca', 'data_criacao']

    def clean(self):
        cleaned_data = super().clean()

        raca = self.cleaned_data['raca']
        data_criacao = self.cleaned_data['data_criacao']

        criacaos_existentes = Criacao.objects.filter(raca=raca, data_criacao=data_criacao)

        if len(criacaos_existentes) > 0:
            raise ValidationError("Já existe uma coleta cadastrada para esta criação nesta data.")