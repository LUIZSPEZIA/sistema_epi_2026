from django.db import models
from django.utils import timezone

class EPI(models.Model):
    CATEGORIAS = [
        ('capacete', 'Capacete'),
        ('luva', 'Luva'),
        ('oculos', 'Óculos'),
        ('bota', 'Bota'),
        ('mascara', 'Máscara'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome do EPI")
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='outro')
    ca = models.CharField(max_length=50, verbose_name="C.A.")
    quantidade = models.PositiveIntegerField(default=0)
    validade = models.DateField(null=True, blank=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.categoria})"
    
    class Meta:
        verbose_name = "EPI"
        verbose_name_plural = "EPIs"
        ordering = ['nome']
