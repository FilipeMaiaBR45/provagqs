from django.db import models


class Criacao(models.Model):
    id = models.AutoField(primary_key=True)
    raca = models.CharField(max_length=50)
    data_criacao = models.DateField(blank=True, null=True, auto_now=True)


class Coleta(models.Model):
    id = models.AutoField(primary_key=True)
    criacao = models.ForeignKey(Criacao, on_delete=models.CASCADE)
    data = models.DateField(blank=True, null=True, auto_now=True)
    quantidade = models.IntegerField()