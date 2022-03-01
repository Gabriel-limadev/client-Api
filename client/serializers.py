from rest_framework import serializers
from .models import Client

from client.validators import *

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    # Validações
    def validate(self, data):
        """Validate studant data """
        if not valid_name(data['name']):
            raise serializers.ValidationError({'name': 'The name field cannot contain numbers'})

        # Validate CPF
        if not valid_cpf_characters(data['cpf']):
            raise serializers.ValidationError({'cpf': 'The name field must have 11 digits'})
        elif not valid_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF entered does not exist'})
        
        # Validate RG
        if not valid_rg(data['rg']):
            raise serializers.ValidationError({'rg': 'The name field must have 9 digits'})

        # Validate Smartphone
        if not valid_smartphone(data['smartphone']):
            raise serializers.ValidationError({'smartphone':'The name field must follow this pattern: 11 99999-9999(respecting space and hyphen).'})

        return data