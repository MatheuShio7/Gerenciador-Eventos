from django.shortcuts import render, redirect
from .forms import EventoForm
from .models import Evento

def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.criador = request.user
            evento.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/criar_evento.html', {'form': form})

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})