# apps->targets->views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Target
from .serializers import TargetSerializer

class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

    def create(self, request, *args, **kwargs):
        return Response(
            {"detail": "Creating goals separately is not allowed."},
            status=status.HTTP_403_FORBIDDEN
        )
