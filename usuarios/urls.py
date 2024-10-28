from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('principal/', views.pagina_principal, name='pagina_principal'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('excluir-conta/', views.excluir_conta, name='excluir_conta'),
]  