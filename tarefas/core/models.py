from django.db import models

class TarefaModel(models.Model):
  titulo = models.CharField(max_length=200)
  inicio = models.DateField('Inicio')
  conclusao = models.DateField('Conclusao')
  descricao = models.CharField(max_length=200)
  categoria = models.CharField(max_length= 50)


def __str__(self):
    return self.titulo
