from django.urls import path
from .import views

urlpatterns = [
    # Home
    path('', views.CadastroPaciente, name='CadastroPaciente'),
    path('AlterarPaciente', views.AlterarPaciente, name='AlterarPaciente'),
    path('VisualizarPaciente', views.VisualizarPaciente, name='VisualizarPaciente'),
    path('ExcluirPaciente', views.ExcluirPaciente, name='ExcluirPaciente'),
]