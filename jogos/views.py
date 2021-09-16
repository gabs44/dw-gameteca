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

        return redirect('listagem-jogo')
    dados = {'generos': models.Genero.objects.all(), 'plataformas': models.Plataforma.objects.all(),
             'desenvolvedores': models.Desenvolvedor.objects.all()}
    return render(request, 'cadastro_jogo.html', dados)


def edit(request, pk):
    jogo = models.Jogo.objects.get(id=pk)

    if jogo.dono != request.user:
        return redirect('detalhe-jogo', pk)

    if request.method == "POST":
        capa = request.FILES.get('capa')
        if capa is not None:
            jogo.capa = capa

        dados = request.POST

        jogo.nome = dados.get('nome')
        jogo.lancamento = dados.get('lancamento')
        jogo.enredo = dados.get('enredo')
        jogo.critica = dados.get('critica')
        jogo.avaliacao = int(dados.get('avaliacao'))

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

        jogo.generos.set(generos)
        jogo.desenvolvedores.set(desenvolvedores)
        jogo.plataformas.set(plataformas)

        jogo.save()

        return redirect('detalhe-jogo', pk)

    lancamento = str(jogo.lancamento)
    dados = {
        'generos': models.Genero.objects.all(),
        'plataformas': models.Plataforma.objects.all(),
        'desenvolvedores': models.Desenvolvedor.objects.all(),
        'notas': [1, 2, 3, 4, 5],
        'jogo': jogo,
        'generos_marcados': jogo.generos.all(),
        'plataformas_marcados': jogo.plataformas.all(),
        'desenvolvedores_marcados': jogo.desenvolvedores.all(),
        'lancamento': lancamento,
    }
    return render(request, 'atualizacao_jogo.html', dados)


def list(request):
    dados = {'jogos': models.Jogo.objects.filter(dono=request.user)}
    return render(request, 'lista_jogo.html', dados)


def detail(request, pk):
    jogo = models.Jogo.objects.get(id=pk)
    return render(request, 'detalhe_jogo.html', {'jogo': jogo})


def delete(request, pk):
    jogo = models.Jogo.objects.get(id=pk)
    if jogo.dono != request.user:
        return redirect('detalhe-jogo', pk)
    jogo.delete()
    return redirect('listagem-jogo')

