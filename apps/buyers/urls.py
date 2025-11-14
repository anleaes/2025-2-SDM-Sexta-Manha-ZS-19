from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'buyers'

router = routers.DefaultRouter()
# 'compradores' será o nome base na URL
router.register('', views.BuyerViewSet, basename='compradores') 

urlpatterns = [
    path('', include(router.urls) )
]