from django.urls import path
from .import views

urlpatterns = [
    path('', views.CadastrarPaciente, name='CadastrarPaciente'),
    path('AlterarPaciente', views.AlterarPaciente, name='AlterarPaciente'),
    path('VisualizarPaciente', views.VisualizarPaciente, name='VisualizarPaciente'),
    path('ExcluirPaciente', views.ExcluirPaciente, name='ExcluirPaciente'),
]