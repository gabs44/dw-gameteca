from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jogo/novo/', views.create, name='cadastro-jogo'),
    path('jogos/', views.list, name='listagem-jogo'),
    path('jogos/editar/<int:pk>', views.edit, name='atualizacao-jogo'),
    path('jogo/<int:pk>', views.detail, name='detalhe-jogo'),
    path('jogo/excluir/<int:pk>', views.delete, name='remove-jogo'),
]
