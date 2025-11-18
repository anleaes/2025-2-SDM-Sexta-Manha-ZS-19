from rest_framework import serializers
from .models import Item
# Serializer para os Itens do Leilão
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'