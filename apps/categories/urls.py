from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'categories'

# O DefaultRouter cria automaticamente as rotas para GET, POST, PUT, DELETE
router = routers.DefaultRouter()
router.register('', views.CategoryViewSet, basename='categorias')

urlpatterns = [
    path('', include(router.urls) )
]