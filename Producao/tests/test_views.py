from django.test import Client, TestCase

from Producao.models import Coleta


class ProducaoViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Coleta.objects.create(criacao='Abelha rainha', data="0000-00-00", quantidade=50)
    
  
    def test_criar_coleta_template(self):
        client = Client()

        data = {
            'criacao': 'Abelha rainha',
            'data_coleta': '2023-06-30',
            'quantidade': 50
        }

        # URL reversa para a view de criação de Coleta
        url = reverse('criacao_coleta')

        response = client.post(url, data)

        self.assertEquals(response.status_code, 201)
        self.assertTemplateUsed(response, 'Produto/criacao_coleta')


    def test_editar_coleta_template(self):
        client = Client()

        data = {
            'id': 1,
            'criacao': 'Abelha rainha',
            'data_coleta': '2023-06-30',
            'quantidade': 50
        }

        # URL reversa para a view de criação de Coleta
        url = reverse('editar_coleta')

        response = client.post(url, data)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Produto/editar_coleta')



    def test_exibir_relatorio_coleta(self):
        client = Client()

        url = reverse('relatorio_coleta')

        response = client.get(url)

        self.assertContains(response, "Janeiro: 100")
        self.assertContains(response, "Dezembro: 100")
        self.assertContains(response, "Novembro: 100")
        self.assertContains(response, "Outubro: 100")
        self.assertContains(response, "Setembro: 100")
        self.assertContains(response, "Agosto: 100")
        self.assertContains(response, "Julho: 100")
        self.assertContains(response, "Junho: 100")
        self.assertContains(response, "Maio: 100")
        self.assertContains(response, "Abril: 100")
        self.assertContains(response, "Março: 100")
        self.assertContains(response, "Fevereiro: 100")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Produto/relatorio_coleta')


        




    def test_listar_produto_url(self):
        response = self.client.get(reverse("Producao:index"))
        self.assertEquals(response.status_code, 200)
    
    def test_listar_produto_template(self):
        response = self.client.get(reverse('Producao:cadastro_coleta'))
        self.assertTemplateUsed(response, 'cadastro/coleta.html')

    def test_listar_produto_all(self):
        response = self.client.get(reverse('Producao:cadastro_criacao'))
        self.assertEquals(len(response.context['cadastro_criacao']), 5)
    
      