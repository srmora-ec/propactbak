from rest_framework import serializers
from .models import Clausula, Contrato

class ClausulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clausula
        fields = '__all__'


class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'
