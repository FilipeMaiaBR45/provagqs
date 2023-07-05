from datetime import timezone
from django.test import TestCase

from Producao.models import Coleta, Criacao

class ColetaFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
     Criacao.objects.create(raca="Abelha africana", data_criacao="0000-00-00")
     Coleta.objects.create(criacao="Abelha rainha", data="0000-00-00", quantidade=50)

    def test_validacao_data_coleta_create(self):
        data_passada = timezone.now().date() - timezone.timedelta(days=1)
        data_futura = timezone.now().date() + timezone.timedelta(days=1)

        form_data_passada = {'criacao': 'Abelha rainha', 'data_coleta': data_passada, 'quantidade': 50}
        form_data_futura = {'criacao': 'Abelha rainha', 'data_coleta': data_futura, 'quantidade': 50}

        form_passada = ColetaForm(data=form_data_passada)
        form_futura = ColetaForm(data=form_data_futura)

        self.assertTrue(form_passada.is_valid())
        self.assertFalse(form_futura.is_valid())

    def test_validacao_data_coleta_(self):
        coleta = Coleta.objects.create(criacao='Abelha rainha', data_coleta=timezone.now().date(), quantidade=50)
        form_data_passada = {'criacao': 'Abelha rainha', 'data_coleta': coleta.data_coleta - timezone.timedelta(days=1), 'quantidade': 50}
        form_data_futura = {'criacao': 'Abelha rainha', 'data_coleta': coleta.data_coleta + timezone.timedelta(days=1), 'quantidade': 50}

        form_passada = ColetaForm(data=form_data_passada)
        form_futura = ColetaForm(data=form_data_futura)

        self.assertTrue(form_passada.is_valid())
        self.assertFalse(form_futura.is_valid())