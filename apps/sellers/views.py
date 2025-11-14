from rest_framework import viewsets
from .models import Seller
from .serializer import SellerSerializer

# Create your views here.
class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
