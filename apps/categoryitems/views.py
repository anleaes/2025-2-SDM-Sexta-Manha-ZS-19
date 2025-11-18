from rest_framework import viewsets
from .models import CategoryItem
from .serializer import CategoryItemSerializer


class CategoryitemViewSet(viewsets.ModelViewSet):
    queryset = CategoryItem.objects.all()
    serializer_class = CategoryItemSerializer
