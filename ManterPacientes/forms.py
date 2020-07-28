from django import forms

from .models import Paciente

class PacienteForm(forms.ModelsForm):

    class Meta:
        model = Paciente
        fields = ('Nome','Data de Nascimento', "Tipo de Teste","Resultado do Teste")

