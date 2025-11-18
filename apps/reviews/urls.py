from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'reviews'

router = routers.DefaultRouter()
# 'avaliacoes' será o nome base na URL
router.register('', views.ReviewViewSet, basename='avaliacoes') 

urlpatterns = [
    path('', include(router.urls) )
]