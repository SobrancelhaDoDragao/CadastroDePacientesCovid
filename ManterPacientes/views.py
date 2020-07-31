from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm
from django.contrib import messages


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

def VisualizarPaciente(request):
    # Recuperando todos os pacientes do banco
    pacientes = Paciente.objects.all()
    return render(request, 'VisualizarPaciente.html',{'Pacientes':pacientes})

def AlterarPaciente(request,id):

    # Recuperando um paciente especifico 
    paciente = Paciente.objects.get(id=id)
    # Preenchendo os dados do formulário com os dados do paciente
    Formulario = PacienteForm(instance=paciente)

    # Quando o formulário já foi submetido
    if request.method == 'POST':
        
        Formulario = PacienteForm(request.POST, instance=paciente)

        if Formulario.is_valid():
            # Salvando dados do formulário no model corespondente 
            Formulario.save()
            return redirect("VisualizarPaciente")
    else:
        return render(request,'AlterarPaciente.html',{'PacienteForm':Formulario})

def ExcluirPaciente(request,id):
    paciente = Paciente.objects.get(id=id)
    paciente.delete()

    messages.info(request, 'Paciente deletado com sucesso')

    return redirect("VisualizarPaciente")
