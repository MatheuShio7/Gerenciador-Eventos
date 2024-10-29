from django import forms
from django.utils import timezone
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.data_hora:
            # Formata a data/hora para o formato correto ao carregar o formulário
            self.initial['data_hora'] = self.instance.data_hora.strftime('%Y-%m-%dT%H:%M')

    def clean_data_hora(self):
        data_hora = self.cleaned_data.get('data_hora')
        if data_hora and data_hora < timezone.now():
            raise forms.ValidationError("A data e hora não podem ser no passado.")
        return data_hora
