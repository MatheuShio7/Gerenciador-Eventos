from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Usuario

class UsuarioForm(UserCreationForm):
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