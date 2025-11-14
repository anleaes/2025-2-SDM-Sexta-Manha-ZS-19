from rest_framework import viewsets
from .models import Buyer
from .serializer import BuyerSerializer


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
