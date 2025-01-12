# apps->targets->serializers.py

from rest_framework import serializers
from .models import Target
from apps.missions.models import Mission

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = [
            'id', 'mission', 'name', 'country', 'notes', 'status',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['mission', 'created_at', 'updated_at']

    def validate(self, attrs):

        target_instance = self.instance
        new_status = attrs.get('status')

        if target_instance and target_instance.status == Target.STATUS_COMPLETE:
            if 'notes' in attrs:
                raise serializers.ValidationError("Objective completed; notes cannot be changed.")

        if target_instance and target_instance.mission.status == Mission.STATUS_COMPLETE:
            raise serializers.ValidationError("Mission completed; cannot change objective.")

        if new_status == Target.STATUS_COMPLETE and target_instance and target_instance.status == Target.STATUS_ASSIGNED:
            pass

        return attrs

    def update(self, instance, validated_data):
        old_status = instance.status
        new_status = validated_data.get('status', old_status)

        updated_target = super().update(instance, validated_data)

        if old_status == Target.STATUS_ASSIGNED and new_status == Target.STATUS_COMPLETE:

            mission = updated_target.mission
            if mission.all_targets_completed():

                mission.status = mission.STATUS_COMPLETE
                mission.save()

        return updated_target
