from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from usuarios.form import UsuarioForm, UsuarioEditForm


def cadastra_usuario(request):
    formulario = UsuarioForm(request.POST or None)
    dados = {'form': formulario}

    if formulario.is_valid():
        formulario.save()
        return redirect('cadastro-usuario')

    return render(request, 'cadastro_usuario.html', dados)


def atualiza_usuario(request):
    formulario = UsuarioEditForm(request.POST or None, instance=request.user)
    dados = {'form': formulario}

    if formulario.is_valid():
        formulario.save()
        return redirect('cadastro-usuario')
    return render(request, 'atualizacao_usuario.html', dados)


def editar_senha(request):
    if request.method == 'POST':
        formulario = PasswordChangeForm(request.user, request.POST)
        if formulario.is_valid():
            user = formulario.save()
            update_session_auth_hash(request, user)
            return redirect('atualizacao-usuario')
    else:
        formulario = PasswordChangeForm(request.user)
    return render(request, 'edicao_senha.html', {'form': formulario})


def login_usuario(request):
    if request.method == "POST":
        dados = request.POST
        user = User.objects.get(email=dados.get('Email'))
        authenticated_user = authenticate(username=user.username, password=dados.get('Senha'))
        if authenticated_user is None:
            return redirect('login')
        login(request, authenticated_user)
        return redirect('index')
    if request.user:
        print(request.user)
    return render(request, 'login.html')


def logout_usuario(request):
    logout(request)
    return redirect('login')
