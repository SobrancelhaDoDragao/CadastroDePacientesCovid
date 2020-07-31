from django import forms

from .models import Paciente

class PacienteForm(forms.ModelForm):

    NomeCompleto = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome completo','class':'form-control'}))
    DataNascimento = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'type':'date','class':'form-control'}))
    
    class Meta:
        model = Paciente
        fields = ('NomeCompleto','DataNascimento', "TipoTeste","ResultadoTeste")
       