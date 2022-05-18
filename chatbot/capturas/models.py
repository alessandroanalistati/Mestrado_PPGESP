from django.db import models

# Create your models here.
class Captura(models.Model):        
    code = models.CharField(max_length=15)   # para utilizar no lucar do ID - tornar o sistema mais seguro.
    code_user = models.CharField(max_length=15) # codigo do usuário - cada usuario tera seu código.
    ativo = models.IntegerField() # alunos ativos ou não.
    name = models.CharField(max_length=100) # nome do aluno
    idade = models.IntegerField() # idade
    sexo = models.CharField(max_length=10) # sexo
    email = models.CharField(max_length=100) # email
    cel = models.CharField(max_length=15) # telefone celular
    telfixo = models.CharField(max_length=10) # telefone fixo
    cep = models.CharField(max_length=10) # cep 
    estado = models.CharField(max_length=50) # estado
    cidade = models.CharField(max_length=100) # cidade
    bairro = models.CharField(max_length=100) # bairro
    endereco = models.CharField(max_length=200) # endereço
    numero = models.CharField(max_length=5) # número
    nomecurso = models.CharField(max_length=200) # nome do curso que o aluno cursa
    iniciocursoano = models.IntegerField(10) # ano que inicio o curso
    simestreatual = models.IntegerField(50) # simestre atual
    ensino_medio = models.IntegerField(50) # particular/publico
    trabalha =  models.IntegerField()  # trabalha durante o dia?  sim/não
    filhos =  models.IntegerField()  # tem filhos? sim/não
    possuinotbook =  models.IntegerField()  # possui PC, notebook, cel? sim/não    
    obs = models.CharField(max_length=200) # informação que o admin podera usar.

    def __str__(self):
        return self.code

