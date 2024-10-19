from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UsuarioForm
from eventos.models import Evento


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


def pagina_principal(request):
    eventos_publicos = Evento.objects.filter(visibilidade='publico').exclude(criador=request.user)
    eventos_usuario = Evento.objects.filter(criador=request.user)
    
    return render(request, 'usuarios/pagina_principal.html', {
        'eventos_publicos': eventos_publicos,
        'eventos_usuario': eventos_usuario
    })