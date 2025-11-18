from rest_framework import serializers
from .models import CategoryItem

# Serializer para a Tabela de Ligação M2M

class CategoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryItem
        fields = '__all__'