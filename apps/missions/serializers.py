# apps->missions->serializers.py

from rest_framework import serializers
from .models import Mission
from apps.targets.models import Target
from apps.targets.serializers import TargetSerializer

class MissionSerializer(serializers.ModelSerializer):


    targets = TargetSerializer(many=True, required=False)

    class Meta:
        model = Mission
        fields = [
            'id',
            'cat',
            'status',
            'targets',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['status', 'created_at', 'updated_at']

    def validate(self, attrs):
        """
        Mission level validation, if targets are passed in the request, then it must be from 1 to 3.
        """
        targets_data = self.initial_data.get('targets', [])
        if not isinstance(targets_data, list):
            raise serializers.ValidationError({"targets": "Targets must be a list."})

        if len(targets_data) == 0:
            raise serializers.ValidationError({"targets": "Minimum 1 target per mission."})
        if len(targets_data) > 3:
            raise serializers.ValidationError({"targets": "Maximum 3 targets per mission."})

        return attrs

    def create(self, validated_data):
        cat = validated_data.get('cat')

        if Mission.objects.filter(cat=cat, status=Mission.STATUS_ASSIGNED).exists():
            raise serializers.ValidationError(
                {"detail": "This cat already has a mission assigned to it. Complete it before creating a new one."}
            )

        mission = Mission.objects.create(cat=cat)

        targets_data = self.initial_data.get('targets', [])
        for target_dict in targets_data:
            Target.objects.create(
                mission=mission,
                name=target_dict['name'],
                country=target_dict.get('country', ''),
                notes=target_dict.get('notes', ''),
                status=Target.STATUS_ASSIGNED
            )

        return mission


    def to_representation(self, instance):

        data = super().to_representation(instance)

        data['targets'] = TargetSerializer(instance.targets.all(), many=True).data 
        return data

    def update(self, instance, validated_data):

        if instance.status == Mission.STATUS_COMPLETE:
            raise serializers.ValidationError("Unable to update a completed mission.")

        return super().update(instance, validated_data) 
