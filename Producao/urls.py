from django.urls import path

from Producao import views

app_name = 'producao'

urlpatterns = [
    
    path('criar/', views.criacoes, name='criar'),
    # path('criar-cbv/', views.CriarProduto.as_view(), name='criar_cbv'),

    # path('listar/', views.listar_produtos, name='listar'),
    # path('listar-cbv/', views.ListarProdutos.as_view(), name='listar_cbv'),

    # path('listar-falta/', views.listar_produtos_falta, name='listar_falta'),
    # path('listar-falta-cbv/', views.ListarProdutosFalta.as_view(), name='listar_falta_cbv'),

    # path('detalhes/<int:pk>', views.detalhes_produto, name='detalhes'),
    # path('detalhes-cbv/<int:pk>', views.DetalhesProduto.as_view(), name='detalhes_cbv'),

]