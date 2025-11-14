from rest_framework import serializers
from .models import Seller
# Serializer para Vendedores

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'