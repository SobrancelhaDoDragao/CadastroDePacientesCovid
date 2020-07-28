from django.shortcuts import render
from .models import Paciente

# Create your views here.
def CadastrarPaciente(request):
    return render(request, 'CadastrarPaciente.html')

def AlterarPaciente(request):
    return render(request, 'AlterarPaciente.html')

def VisualizarPaciente(request):

    pacientes = Paciente.objects.all()
    return render(request, 'VisualizarPaciente.html',{'Pacientes':pacientes})

def ExcluirPaciente(request):
    return render(request, 'ExcluirPaciente.html')
