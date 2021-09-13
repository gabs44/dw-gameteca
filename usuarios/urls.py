from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('usuario/cadastro/', views.cadastra_usuario, name='cadastro-usuario'),
    path('usuario/minha-conta/', views.atualiza_usuario, name='atualizacao-usuario'),
    path('usuario/editar-senha', views.editar_senha, name='editar-senha')
]
