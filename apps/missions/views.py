from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Mission
from .serializers import MissionSerializer
from rest_framework.decorators import action
from apps.cats.models import Cat

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        if mission.status != Mission.STATUS_COMPLETE:
            return Response(
                {"detail": "It is possible to delete a mission that has not been completed."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=['patch'], url_path='mark-as-complete')
    def mark_as_complete(self, request, pk=None):
        mission = self.get_object()

        if mission.status == Mission.STATUS_COMPLETE:
            return Response(
                {"detail": "The mission is already completed."},
                status=status.HTTP_400_BAD_REQUEST
            )

        mission.status = Mission.STATUS_COMPLETE
        mission.save()

        targets = mission.targets.all()
        for t in targets:
            t.status = t.STATUS_COMPLETE
            t.save()

        serializer = self.get_serializer(mission)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'], url_path='assign-cat')
    def assign_cat(self, request, pk=None):

        mission = self.get_object()

        if mission.status == Mission.STATUS_COMPLETE:
            return Response(
                {"detail": "It is not possible to assign a cat to a completed mission."},
                status=status.HTTP_400_BAD_REQUEST
            )

        cat_id = request.data.get('cat')
        if not cat_id:
            return Response({"detail": "cat is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cat_obj = Cat.objects.get(pk=cat_id)
        except Cat.DoesNotExist:
            return Response({"detail": "Such a cat does not exist."}, status=status.HTTP_404_NOT_FOUND)

        if Mission.objects.filter(cat=cat_obj, status=Mission.STATUS_ASSIGNED).exists():
            return Response(
                {"detail": "This cat already has an assigned mission."},
                status=status.HTTP_400_BAD_REQUEST
            )

        mission.cat = cat_obj
        mission.save()

        serializer = self.get_serializer(mission)
        return Response(serializer.data, status=status.HTTP_200_OK) 
