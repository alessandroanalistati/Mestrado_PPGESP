from django.db import models

# Create your models here.
class Usuario(models.Model):
    code = models.CharField(max_length=15)   # para utilizar no lucar do ID - tornar o sistema mais seguro.
    ativo = models.IntegerField() # alunos ativos ou não.
    name = models.CharField(max_length=100) # nome do usuário.
    email = models.CharField(max_length=50) # e-mail do usuário.
    login = models.CharField(max_length=50) # login do usuario.
    passord = models.CharField(max_length=10) # senha.

def __str__(self):
    return self.question
