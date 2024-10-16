from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UsuarioForm

# View da home
def home(request):
    return render(request, 'usuarios/home.html')


# View de cadastro
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


# View de login
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
    return render(request, 'usuarios/pagina_principal.html')