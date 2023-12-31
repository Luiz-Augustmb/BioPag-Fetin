from django.urls import path

from . import views


urlpatterns = [
    #ULR'S das página (render)
    path('', views.index, name='index'),
    path('segundaAplicacao/', views.segundaAplicacao, name='segundaAplicacao'),
    path('cadastroDigital/', views.cadastroDigital, name='cadastroDigital'),
    path('entrada_Valor/', views.entrada_Valor, name='entrada_Valor'),
    path('forma_Pagamento/', views.forma_Pagamento, name='forma_Pagamento'),
    path('opcao_Pagamento/', views.opcao_Pagamento, name='opcao_Pagamento'),
    path('verifica_Digital/', views.verifica_Digital, name='verifica_Digital'),
    path('pag_Aprovado/', views.pag_Aprovado, name='pag_Aprovado'),
    path('pag_Negado/', views.pag_Negado, name='pag_Negado'),
    path('deletaDigital/', views.deletaDigital, name='deletaDigital'),
    #Funcionamento da verificação da Digital
    path('verify_fingerprint/', views.verify_fingerprint, name='verify_fingerprint'),
    #Funcionamento  do cadastro de uma nova digital
    path('enroll_fingerprint/<int:fingerprint_id>/', views.enroll_fingerprint, name='enroll_fingerprint'),
    #Funcionamento de esvaziar o banco de dados
    path('limpa_banco/', views.limpa_banco, name='limpa_banco'),
    #Funcionamento de deletar uma digital
    path('deleteDigital/<int:fingerprint_id>/', views.deleteDigital, name='deleteDigital'),

]
