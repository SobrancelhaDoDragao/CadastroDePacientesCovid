from django.db import models

# Create your models here.

class Paciente(models.Model):
    
    Testes = (
        (1,"RT-PCR"),(2,"Sorologia"),(3,"Teste Rápido"),(4,"Antígenos"),(5,"Teste Rápido - Anticorpos")
    )

    Resultados = (
        (1,"Positivo"),(2,"Negativo")
    )

    NomeCompleto = models.CharField(max_length=30)
    DataNascimento = models.DateField()
    TipoTeste = models.CharField(max_length=60, choices=Testes)
    ResultadoTeste = models.CharField(max_length=60,choices=Resultados)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
