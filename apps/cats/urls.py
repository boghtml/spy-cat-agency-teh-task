# apps/cats/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatViewSet

router = DefaultRouter()
router.register(r'cats', CatViewSet, basename='cats')

urlpatterns = [
    path('', include(router.urls)),
]
