# Generated by Django 3.0.8 on 2020-07-27 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManterPacientes', '0002_auto_20200727_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='ResultadoTeste',
            field=models.CharField(choices=[('Positivo', 'Positivo'), ('Negativo', 'Negativo')], max_length=30),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='TipoTeste',
            field=models.CharField(choices=[('RT-PCR', 'RT-PCR'), ('Sorologia', 'Sorologia'), ('Teste Rápido', 'Teste Rápido'), ('Antígenos', 'Antígenos'), ('Teste Rápido - Anticorpos', 'Teste Rápido - Anticorpos')], max_length=30),
        ),
    ]