from django.urls import path
from . import views

urlpatterns = [
    path('usuario/cadastro/', views.cadastra_usuario, name='cadastro-usuario'),
]
