from django.urls import path
from . import views

urlpatterns = [
    path('criar_evento/', views.criar_evento, name='criar_evento'),
    path('evento/<int:evento_id>/', views.detalhes_evento, name='detalhes_evento'),
    path('evento/<int:evento_id>/editar/', views.editar_evento, name='editar_evento'),
    path('evento/<int:evento_id>/inscrever/', views.inscrever_evento, name='inscrever_evento'),
    path('evento/<int:evento_id>/desinscrever/', views.desinscrever_evento, name='desinscrever_evento'),
    path('evento/<int:evento_id>/deletar/', views.deletar_evento, name='deletar_evento'),
    path('evento/inscricao/<int:evento_id>/', views.inscricao_evento, name='inscricao_evento'),
] 