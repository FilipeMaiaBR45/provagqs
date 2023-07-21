from django.urls import path

from Producao import views

app_name = 'producao'

urlpatterns = [
    
    path('listar-criacoes/', views.listar_criacoes, name='listar_criacoes'),
    #path('detalhes-criacao/', views.detalhes_criacoes, name='detalhes_criacoes'),
    path('criar-criacao/', views.criar_criacao, name='criar_criacao'),
    #path('deletar-criacao/', views.deletar_criacoe, name='deletar_criacoe'),
    #path('editar-criacao/', views.editar_criacoes, name='editar_criacoes'),

    #------------------------------------------------------------------------
    path('listar-coletas/', views.listar_coletas, name='listar_coletas'),
    path('detalhes-coleta/<int:pk>/', views.detalhes_coleta, name='detalhes_coleta'),
    path('criar-coleta/', views.criar_coleta, name='criar_coleta'),
    path('deletar-coleta/<int:pk>', views.deletar_coleta, name='deletar_coleta'),
    path('editar-coleta/<int:pk>/', views.editar_coleta, name='editar_coleta'),
    path('relatorio-coletas/', views.relatorio_coletas, name='relatorio_coletas'),



    #path('criacoes/', views.listar_criacoes, name='listar_criacoes'),
    # path('criar-cbv/', views.CriarProduto.as_view(), name='criar_cbv'),

    # path('listar/', views.listar_produtos, name='listar'),
    # path('listar-cbv/', views.ListarProdutos.as_view(), name='listar_cbv'),

    # path('listar-falta/', views.listar_produtos_falta, name='listar_falta'),
    # path('listar-falta-cbv/', views.ListarProdutosFalta.as_view(), name='listar_falta_cbv'),

    # path('detalhes/<int:pk>', views.detalhes_produto, name='detalhes'),
    # path('detalhes-cbv/<int:pk>', views.DetalhesProduto.as_view(), name='detalhes_cbv'),

]