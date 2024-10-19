from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventoForm
from .models import Evento


def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.criador = request.user
            evento.save()
            return redirect('pagina_principal')
    else:
        form = EventoForm()
    return render(request, 'eventos/criar_evento.html', {'form': form})


def detalhes_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'eventos/detalhes_evento.html', {'evento': evento})


def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('detalhes_evento', evento_id=evento.id)  # Redireciona para a página de detalhes
    else:
        form = EventoForm(instance=evento)

    return render(request, 'eventos/editar_evento.html', {'form': form, 'evento': evento})