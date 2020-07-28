from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm


def CadastroPaciente(request):
    # O quando formulário já foi submetido
    if request.method == 'POST':
        # Salvando os dados do formulário
        Formulario = PacienteForm(request.POST)
        
        if Formulario.is_valid():
            # Salvando dados do formulário no model corespondente 
            Formulario.save()
            return redirect("VisualizarPaciente")
    else:
        # Criando formulário
        Formulario = PacienteForm()
        return render(request, 'CadastroPaciente.html',{'Formulario':Formulario})

def AlterarPaciente(request):
    return render(request, 'AlterarPaciente.html')

def VisualizarPaciente(request):
    # Recuperando todos os pacientes do banco
    pacientes = Paciente.objects.all()
    return render(request, 'VisualizarPaciente.html',{'Pacientes':pacientes})

def ExcluirPaciente(request):
    return render(request, 'ExcluirPaciente.html')
