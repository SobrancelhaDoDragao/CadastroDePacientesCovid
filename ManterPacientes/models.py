from django.db import models

# Create your models here.

class Paciente(models.Model):
    
    Testes = (
        ("RT-PCR","RT-PCR"),("Sorologia","Sorologia"),("Teste Rápido","Teste Rápido"),("Antígenos","Antígenos"),("Teste Rápido - Anticorpos","Teste Rápido - Anticorpos")
    )

    Resultados = (
        ("Positivo","Positivo"),("Negativo","Negativo")
    )

    NomeCompleto = models.CharField(max_length=30)
    DataNascimento = models.DateField()
    TipoTeste = models.CharField(choices=Testes, max_length=30)
    ResultadoTeste = models.CharField(choices=Resultados, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.NomeCompleto
