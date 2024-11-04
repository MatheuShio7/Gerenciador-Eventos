from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Usuario

class UsuarioForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Primeiro Nome')
    last_name = forms.CharField(max_length=30, required=True, label='Último Nome')
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
    )
    sexo = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Feminino')])

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'data_nascimento', 'sexo']
        help_texts = {
            'username': None,
        }

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')
        if data_nascimento >= timezone.now().date():
            raise ValidationError("A data de nascimento não pode ser no futuro.")
        return data_nascimento 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Removendo a mensagem de ajuda do campo password2 (confirmação de senha)
        self.fields['password2'].help_text = ''


class EditarPerfilForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
    )
    sexo = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Feminino')])

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'data_nascimento', 'sexo']

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')
        if data_nascimento >= timezone.now().date():
            raise ValidationError("A data de nascimento não pode ser no futuro.")
        return data_nascimento 


class AlterarSenhaForm(PasswordChangeForm):
    class Meta:
        model = Usuario
        fields = ['old_password', 'new_password1', 'new_password2']