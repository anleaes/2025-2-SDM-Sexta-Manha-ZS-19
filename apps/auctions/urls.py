from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'auctions'

router = routers.DefaultRouter()
# 'leiloes' será o nome base na URL
router.register('', views.AuctionViewSet, basename='leiloes') 

urlpatterns = [
    path('', include(router.urls) )
]