from rest_framework import serializers
from .models import Payment

# Serializer para a API de Pagamentos

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'