from django.db import models


class Criacao(models.Model):
    id = models.AutoField(primary_key=True)
    raca = models.CharField(blank=False, max_length=50, verbose_name="Raça")
    data_criacao = models.DateField(blank=False, verbose_name="Data")


class Coleta(models.Model):
    id = models.AutoField(primary_key=True)
    criacao = models.ForeignKey(Criacao, on_delete=models.CASCADE, verbose_name="Criação")
    data = models.DateField(blank=True, null=True, verbose_name="Data")
    quantidade = models.IntegerField(verbose_name="Quantidade")