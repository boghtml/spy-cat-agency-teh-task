# apps/cats/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Cat
from .serializers import CatSerializer

class CatViewSet(viewsets.ModelViewSet):

    queryset = Cat.objects.all()
    serializer_class = CatSerializer


    @action(detail=True, methods=['patch'], url_path='update-salary')
    def update_salary(self, request, pk=None):
        cat = self.get_object()
        new_salary = request.data.get("salary")
        if new_salary is None:
            return Response({"detail": "Salary is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cat.salary = float(new_salary)
            cat.save()
        except ValueError:
            return Response({"detail": "Invalid salary value."}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(CatSerializer(cat).data, status=status.HTTP_200_OK)
