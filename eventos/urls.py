from django.urls import path
from . import views

urlpatterns = [
    path('criar_evento/', views.criar_evento, name='criar_evento'),
    path('eventos/', views.lista_eventos, name='lista_eventos'),
]