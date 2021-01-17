from django.db import models

# Create your models here.
class Evento(models.Model):
    codigo = models.IntegerField()
    cod_relatorio = models.IntegerField()
    cod_empresa = models.IntegerField()
    cod_atracao = models.IntegerField()
    local = models.CharField(max_length=60)#MODELO TIPO STRING
    data = models.DateTimeField(auto_now = False)#data e hora
    cidade = models.CharField(max_length=60)#MODELO TIPO STRING
    estado = models.CharField(max_length=60)#MODELO TIPO STRING
    nome = models.CharField(max_length=60)#MODELO TIPO STRING

    def __str__(self):
        return self.nome

