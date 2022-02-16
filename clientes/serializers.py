from rest_framework import serializers
from .models import Cliente

from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    # Validações
    def validate(self, data):
        # Validando Nome
        if nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O campo nome não deve ter números ou caracteres especiais'})

        # Validando CPF
        if not cpf_caracteres_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'O campo CPF deve ter 11 digitos'})
        elif not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'Número de CPF inválido!'})  
        
        # Validando RG 
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O campo RG deve ter 9 digitos'})

        # Validando Celular
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O campo celular deve seguir esse padrão: 11 99999-9999(respeitando o espaço e o traço).'})

        return data