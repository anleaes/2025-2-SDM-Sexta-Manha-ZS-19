from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'payments'

router = routers.DefaultRouter()
router.register('', views.PaymentViewSet, basename='pagamentos') 

urlpatterns = [
    path('', include(router.urls) )
]