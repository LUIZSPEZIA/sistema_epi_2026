from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=120)
    matricula = models.CharField(max_length=14, unique=True)
    cpf = models.CharField(max_length=11, unique=True,blank=True)
    setor = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    cargo = models.CharField(max_length=80, blank=True)
    data_admissao = models.DateField(null=True, blank=True)
    observacoes = models.TextField(blank=True)
    foto_colaborador = models.ImageField(
        upload_to='colaboradores/fotos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.nome} ({self.setor})"