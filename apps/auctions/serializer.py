from rest_framework import serializers
from .models import Auction

# Serializer para a API de Leilões

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'