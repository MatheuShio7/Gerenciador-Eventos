from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'data_hora', 'endereco', 'limite_convidados', 'visibilidade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-nome'}),
            'data_hora': forms.DateTimeInput(attrs={'class': 'form-data-hora', 'type': 'datetime-local'}),
            'endereco': forms.TextInput(attrs={'class': 'form-endereco'}),
            'descricao': forms.Textarea(attrs={'class': 'form-descricao'}),
            'limite_convidados': forms.NumberInput(attrs={'class': 'form-limite-convidados'}),
            'visibilidade': forms.Select(attrs={'class': 'form-visibilidade'}),
        }
        labels = {
            'nome': 'Nome do Evento',
            'data_hora': 'Data e Hora',
            'endereco': 'Endereço',
            'descricao': 'Descrição',
            'limite_convidados': 'Limite de Convidados',
            'visibilidade': 'Visibilidade',
        }