from django.contrib.auth.models import User
from django.db import models


class Genero(models.Model):

    nome = models.CharField(max_length=20)


class Plataforma(models.Model):

    nome = models.CharField(max_length=20)


class Endereco(models.Model):

    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)


class Desenvolvedor(models.Model):

    nome = models.CharField(max_length=50)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)


# Jogo
class Jogo(models.Model):

    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    lancamento = models.DateField()
    generos = models.ManyToManyField(Genero, related_name='generos')
    plataformas = models.ManyToManyField(Plataforma, related_name='plataformas')
    enredo = models.TextField()
    critica = models.TextField()
    avaliacao = models.IntegerField()
    capa = models.FileField(upload_to='imagens')
    desenvolvedores = models.ManyToManyField(Desenvolvedor, related_name='desenvolvedores')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'jogo'
        verbose_name_plural = 'jogos'

