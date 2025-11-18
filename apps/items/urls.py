from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'items'

router = routers.DefaultRouter()
# 'itens' será o nome base na URL
router.register('', views.ItemViewSet, basename='itens') 

urlpatterns = [
    path('', include(router.urls) )
]