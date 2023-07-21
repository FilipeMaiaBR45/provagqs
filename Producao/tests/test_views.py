from django.test import Client, TestCase

from Producao.models import Coleta, Criacao
from django.urls import reverse

from datetime import date



class ProducaoViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        criacao = Criacao.objects.create(raca="Abelha africana", data_criacao="2023-06-20")

        Coleta.objects.create(criacao=criacao, data="2023-06-20", quantidade=50)

    def test_listar_coleta_url(self):
        response = self.client.get(reverse('producao:listar_coletas'))
        self.assertEquals(response.status_code, 200)

    def test_listar_coleta_template(self):
      
        # Enviar uma requisição GET para a view de listagem de coletas
        url = reverse('producao:listar_coletas')
        response = self.client.get(url)

        # Verificar se o status da resposta é 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar se o template correto é usado
        self.assertTemplateUsed(response, 'Producao/coleta_list.html')
    
    def test_listar_todas_coletas(self):
        response = self.client.get(reverse('producao:listar_coletas'))
        self.assertEquals(len(response.context['lista_produtos']), 1)

    #--------------------------------------------------------------------------------------------------

   # def test_detalhes_coleta_url(self):

    #def test_detalhes_coleta_template(self):

    #def test_detalhes_coleta(self):

    #--------------------------------------------------------------------------------------------------


    #def test_deletar_coleta_url(self):

  #  def test_deletar_coleta_template(self):

   # def test_deletar_coleta(self):


    #--------------------------------------------------------------------------------------------------


    def test_criar_coleta_url(self):
        #response = self.client.get(reverse('producao:criar-coleta'))
        data = {
            'criacao': 1,
            'data_coleta': '2023-06-30',
            'quantidade': 50
        }
        url = reverse('producao:criar_coleta')
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Producao/criar_coleta.html')
        nova_coleta = Coleta.objects.filter('criacao': 1, 'data_coleta': '2023-06-30', 'quantidade': 50)
        self.assertEquals(len(nova_coleta), 1)

    #def test_criar_coleta(self):


    #--------------------------------------------------------------------------------------------------


   # def test_editar_coleta_url(self):

    def test_editar_coleta_template(self):
        client = Client()

        data = {
            'id': 1,
            'criacao': 1,
            'data_coleta': '2023-06-30',
            'quantidade': 50
        }

        # URL reversa para a view de criação de Coleta
        url = reverse('producao:editar_coleta', kwargs={'pk': 1})

        response = client.post(url, data)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Producao/editar_coleta.html')

    #def test_editar_coleta(self):

    #--------------------------------------------------------------------------------------------------

   # def test_exibir_relatorio_coleta_url(self):

    def test_exibir_relatorio_coleta_template(self):

    #def test_exibir_relatorio_coleta(self):
        client = Client()

        url = reverse('producao:relatorio_coletas')

        response = client.get(url)

        
        self.assertTemplateUsed(response, 'Producao/relatorio_coletas.html')


    #def setUp(self):
     #   self.client = Client()
     #   self.url = reverse('coleta')

    

    




    
      