from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Usuario


class UsuarioForm(UserCreationForm):
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    sexo = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Feminino')])

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'data_nascimento', 'sexo']


class EditarPerfilForm(forms.ModelForm):
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    sexo = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Feminino')])

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'data_nascimento', 'sexo']  # Inclua todos os campos que você deseja editar


class AlterarSenhaForm(PasswordChangeForm):
    class Meta:
        model = Usuario
        fields = ['old_password', 'new_password1', 'new_password2']