from rest_framework import viewsets
from .models import Seller
from .serializer import SellerSerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all().order_by('name')
    serializer_class = SellerSerializer
