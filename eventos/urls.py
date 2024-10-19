from django.urls import path
from . import views
from .views import editar_evento

urlpatterns = [
    path('criar_evento/', views.criar_evento, name='criar_evento'),
    path('evento/<int:evento_id>/', views.detalhes_evento, name='detalhes_evento'),
    path('evento/<int:evento_id>/editar/', editar_evento, name='editar_evento'),
]