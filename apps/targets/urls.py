from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TargetViewSet

router = DefaultRouter()
router.register(r'targets', TargetViewSet, basename='targets')

urlpatterns = [
    path('', include(router.urls)),
]
