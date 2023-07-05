from django.test import TestCase

from Producao.models import Coleta, Criacao


class ProducaoModelTest(TestCase):
      @classmethod
      def setUpTestData(cls):
          Criacao.objects.create(raca="Abelha africana", data_criacao="0000-00-00")
          Coleta.objects.create(criacao="Abelha africana", data_criacao="2020-12-01", quantidade=50)
          Coleta.objects.create(criacao="Abelha africana", data_criacao="2020-12-02", quantidade=50)
          Coleta.objects.create(criacao="Abelha africana", data_criacao="2020-12-03", quantidade=50)

     
      def test_raca_max_length(self):
        criacao = Criacao.objects.get(id=1)
        max_length = criacao._meta.get_field('raca').max_length
        self.assertEquals(max_length, 50)


      def test_raca_label(self):
        criacao = Criacao.objects.get(id=1)
        label_do_produto = criacao._meta.get_field('raca').verbose_name
        self.assertTrue(label_do_produto == "Raça")

      def test_campos_obrigatorios(self):
         criacao = Criacao()  
         self.assertFalse(criacao.is_valid())


      def test_ordering(self):
        lista_ordenada = [Coleta.objects.get(id=3), Coleta.objects.get(id=2), Coleta.objects.get(id=1)]
        
        coleta = [entry for entry in Coleta.objects.all()]
        self.assertEquals(lista_ordenada, coleta)
