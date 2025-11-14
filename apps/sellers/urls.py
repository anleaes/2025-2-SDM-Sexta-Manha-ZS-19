from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'sellers'

router = routers.DefaultRouter()
# 'vendedores' será o nome base na URL
router.register('', views.SellerViewSet, basename='vendedores') 

urlpatterns = [
    path('', include(router.urls) )
]