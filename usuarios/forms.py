from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForm(UserCreationForm):
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    sexo = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Feminino')])

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'data_nascimento', 'sexo']