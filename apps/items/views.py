from rest_framework import viewsets
from .models import Item
from .serializer import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('title')
    serializer_class = ItemSerializer
