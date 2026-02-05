from rest_framework import serializers
from .models import Colaborador

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = ['id', 'nome', 'matricula', 'cpf', 'setor', 'foto_colaborador']
