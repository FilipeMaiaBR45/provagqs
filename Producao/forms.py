

from django.forms import ValidationError
from Producao.models import Criacao

class CriacaoForm(ModelForm):
    class Meta:
        model = Criacao 
        fields = ['raca', 'data_criacao']

    def clean(self):
        cleaned_data = super().clean()

        raca = self.cleaned_data['raca']
        data_criacao = self.cleaned_data['data_criacao']

        criacao_existentes = Criacao.objects.filter(raca=raca, data_criacao=data_criacao)

        if (len(criacao_existentes) > 0):
            raise ValidationError("Já há um produto deste fornecedor com este nome cadastrado.")