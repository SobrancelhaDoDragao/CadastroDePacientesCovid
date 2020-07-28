from django import forms

from .models import Paciente

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('NomeCompleto','DataNascimento', "TipoTeste","ResultadoTeste")
