from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MissionViewSet

router = DefaultRouter()
router.register(r'missions', MissionViewSet, basename='missions')

urlpatterns = [
    path('', include(router.urls)),
]
