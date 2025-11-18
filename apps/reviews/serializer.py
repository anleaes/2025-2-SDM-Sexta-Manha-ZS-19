from rest_framework import serializers
from .models import Review

# Serializer para as Avaliações de Vendedores

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'