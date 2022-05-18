from django.db import models

# Create your models here.

class Pergunta(models.Model):
    code = models.CharField(max_length=15)   # para utilizar no lucar do ID - tornar o sistema mais seguro.
    code_user = models.CharField(max_length=15) # codigo do usuário - cada usuario tera seu código.
    ativo = models.IntegerField() # alunos ativos ou não.
    code_relacao = models.CharField(max_length=15) # relação com pergunta anteriores.
    pergunta = models.CharField(max_length=500) # possivel perguntas que for feita.
    resposta = models.CharField(max_length=500) # valor devolvido caso a pergunta acima for feita.

def __str__(self):
    return self.question