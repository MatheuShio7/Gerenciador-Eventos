from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('principal/', views.pagina_principal, name='pagina_principal'),
]