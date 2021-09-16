from django.shortcuts import render, redirect
from . import models


def index(request):
    return render(request, 'home.html')


def create(request):
    if request.method == "POST":
        capa = request.FILES.get('capa')
        dados = request.POST

        nome = dados.get('nome')
        lancamento = dados.get('lancamento')
        enredo = dados.get('enredo')
        critica = dados.get('critica')
        avaliacao = int(dados.get('avaliacao'))

        generos = []
        for genero in models.Genero.objects.all():
            genero_id = dados.get(genero.nome)
            if genero_id is not None:
                gen = models.Genero.objects.get(id=genero_id)
                gen.save()
                generos.append(gen)

        desenvolvedores = []
        for desenvolvedor in models.Desenvolvedor.objects.all():
            desenvolvedor_id = dados.get(desenvolvedor.nome)
            if desenvolvedor_id is not None:
                dev = models.Desenvolvedor.objects.get(id=desenvolvedor_id)
                dev.save()
                desenvolvedores.append(dev)

        plataformas = []
        for plataforma in models.Plataforma.objects.all():
            plataforma_id = dados.get(plataforma.nome)
            if plataforma_id is not None:
                plat = models.Plataforma.objects.get(id=plataforma_id)
                plat.save()
                plataformas.append(plat)

        jogo = models.Jogo.objects.create(lancamento=lancamento, avaliacao=avaliacao, enredo=enredo, critica=critica,
                                          nome=nome, capa=capa, dono=request.user)

        jogo.generos.set(generos)
        jogo.desenvolvedores.set(desenvolvedores)
        jogo.plataformas.set(plataformas)

        jogo.save()

        return redirect('cadastro-jogo')  # TODO redirecionar para listagem
    dados = {'generos': models.Genero.objects.all(), 'plataformas': models.Plataforma.objects.all(),
             'desenvolvedores': models.Desenvolvedor.objects.all()}
    return render(request, 'cadastro_jogo.html', dados)
