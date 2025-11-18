from rest_framework import viewsets
from .models import Item
from .serializer import ItemSerializer

# ViewSet será responsável por gerenciar todas as requisições da API para Itens
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('title')
    serializer_class = ItemSerializer
