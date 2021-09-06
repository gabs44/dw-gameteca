from django.shortcuts import render


def cadastra_usuario(request):
    return render(request, 'cadastro_usuario.html', {})
