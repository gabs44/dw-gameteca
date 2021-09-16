from django.contrib import admin
from .models import Genero, Plataforma, Endereco, Desenvolvedor, Jogo


admin.site.register((Genero, Plataforma, Endereco, Desenvolvedor, Jogo))
