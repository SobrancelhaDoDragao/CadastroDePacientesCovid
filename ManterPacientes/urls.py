from django.urls import path
from .import views

urlpatterns = [
    # Home
    path('CadastroPaciente', views.CadastroPaciente, name='CadastroPaciente'),
    path('AlterarPaciente/<int:id>', views.AlterarPaciente, name='AlterarPaciente'),
    path('', views.VisualizarPaciente, name='VisualizarPaciente'),
    #path('ExcluirPaciente/<int:id>', views.ExcluirPaciente, name='ExcluirPaciente'),
]