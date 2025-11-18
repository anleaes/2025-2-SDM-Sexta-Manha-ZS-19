from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'bids'

router = routers.DefaultRouter()
# 'lances' será o nome base na URL
router.register('', views.BidViewSet, basename='lances') 

urlpatterns = [
    path('', include(router.urls) )
]