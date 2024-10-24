from django.db import models
from usuarios.models import Usuario

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data_hora = models.DateTimeField()
    endereco = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    limite_convidados = models.PositiveIntegerField()
    visibilidade = models.CharField(max_length=7, choices=[('publico', 'Público'), ('privado', 'Privado')])
    criador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    convidados = models.ManyToManyField(Usuario, related_name='eventos_inscritos', blank=True)