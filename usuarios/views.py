from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UsuarioForm, EditarPerfilForm, AlterarSenhaForm
from eventos.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


def home(request):
    return render(request, 'usuarios/home.html')


def cadastro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Loga o usuário automaticamente após o cadastro
            return redirect('pagina_principal')  # Redireciona para a página principal
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('pagina_principal')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})


@login_required
def pagina_principal(request):
    # Buscar eventos criados pelo usuário OU nos quais o usuário está inscrito (Meus Eventos)
    eventos_usuario = Evento.objects.filter(
        Q(criador=request.user) | Q(convidados=request.user)
    ).distinct()

    # Buscar eventos públicos onde o usuário NÃO está inscrito e que ele não criou
    eventos_publicos = Evento.objects.filter(visibilidade='publico').exclude(
        Q(convidados=request.user) | Q(criador=request.user)
    )

    context = {
        'eventos_usuario': eventos_usuario,  # Meus eventos (criados ou inscritos)
        'eventos_publicos': eventos_publicos,  # Eventos públicos (não inscritos)
    }

    return render(request, 'usuarios/pagina_principal.html', context)


@login_required
def perfil_usuario(request):
    return render(request, 'usuarios/perfil.html', {'usuario': request.user})


@login_required
def editar_perfil(request):
    user_form = EditarPerfilForm(instance=request.user)
    senha_form = AlterarSenhaForm(request.user)  # Instância do formulário para alterar senha

    if request.method == 'POST':
        # Verifica se o formulário de edição de perfil foi enviado
        if 'salvar' in request.POST:
            user_form = EditarPerfilForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Seu perfil foi atualizado com sucesso!')
                return redirect('perfil_usuario')
        
        # Verifica se o formulário de alteração de senha foi enviado
        elif 'alterar_senha' in request.POST:
            senha_form = AlterarSenhaForm(request.user, request.POST)
            if senha_form.is_valid():
                user = senha_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Sua senha foi alterada com sucesso!')
                return redirect('perfil_usuario')

    return render(request, 'usuarios/editar_perfil.html', {
        'user_form': user_form,
        'senha_form': senha_form,
    })


@login_required
def excluir_conta(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)  # Desloga o usuário após a exclusão da conta
        return redirect('home')  # Redireciona para uma página inicial ou de confirmação