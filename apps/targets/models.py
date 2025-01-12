# apps->targets->models.py

from django.db import models
from apps.missions.models import Mission

class Target(models.Model):
    STATUS_ASSIGNED = 'assigned'
    STATUS_COMPLETE = 'complete'
    STATUS_CHOICES = [
        (STATUS_ASSIGNED, 'Assigned'),
        (STATUS_COMPLETE, 'Complete'),
    ]

    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='targets')
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_ASSIGNED)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Target #{self.id}: {self.name}"

    def can_edit_notes(self):

        return (self.status == self.STATUS_ASSIGNED 
                and self.mission.status == Mission.STATUS_ASSIGNED)
