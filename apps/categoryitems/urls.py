from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'categoryitems'

router = routers.DefaultRouter()
# 'itens_categoria' será o nome base na URL
router.register('', views.CategoryitemViewSet, basename='itens_categoria') 

urlpatterns = [
    path('', include(router.urls) )
]