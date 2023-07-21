from django.forms import ValidationError
from django.test import TestCase

from Producao.models import Coleta, Criacao



class ProducaoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        criacao1 = Criacao.objects.create(raca="Abelha africana", data_criacao="2020-06-20")
        Coleta.objects.create(criacao=criacao1, data="2020-12-01", quantidade=50)
        Coleta.objects.create(criacao=criacao1, data="2020-12-02", quantidade=50)
        Coleta.objects.create(criacao=criacao1, data="2020-12-03", quantidade=50)

    def test_raca_max_length(self):
        criacao = Criacao.objects.get(id=1)
        max_length = criacao._meta.get_field('raca').max_length
        self.assertEquals(max_length, 50)

    def test_raca_label(self):
        criacao = Criacao.objects.get(id=1)
        label_do_produto = criacao._meta.get_field('raca').verbose_name
        self.assertTrue(label_do_produto == "Raça")

  

    def test_ordering(self):
        lista_ordenada = [
            Coleta.objects.get(id=3),
            Coleta.objects.get(id=2),
            Coleta.objects.get(id=1)
        ]
        
        coleta = Coleta.objects.all()
        self.assertEquals(lista_ordenada, coleta)