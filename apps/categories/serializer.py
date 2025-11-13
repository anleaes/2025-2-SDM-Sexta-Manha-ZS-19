# Serializer das categorias

from .models import Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    # Serializer responsável por converter os objetos de Categoria para JSON
    class Meta:
        model = Category
        fields = '__all__'
        # Garante que o ID não seja modificado manualmente
        read_only_fields = ['id']