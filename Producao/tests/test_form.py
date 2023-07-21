from datetime import timezone
from django.test import TestCase
from datetime import date, timedelta

from Producao.models import Coleta, Criacao
from Producao.forms import ColetaForm

class ColetaFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
     criacao = Criacao.objects.create(raca="Abelha africana", data_criacao="2023-06-20")
     Coleta.objects.create(criacao=criacao, data="2023-04-20", quantidade=50)

    def test_validacao_data_coleta_ok(self):
        form = ColetaForm(data={'criacao': 1, 'data': '2023-06-28', 'quantidade': 100})
        self.assertTrue(form.is_valid())

    def test_validacao_data_coleta_not_ok(self):
        form1 = ColetaForm(data={'criacao': 1, 'data': '2023-04-20', 'quantidade': 100})
        self.assertFalse(form1.is_valid())
        form2 = ColetaForm(data={'criacao': 1, 'data': '2030-04-20', 'quantidade': 100})
        self.assertFalse(form2.is_valid())


    