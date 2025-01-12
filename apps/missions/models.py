from django.db import models
from apps.cats.models import Cat


class Mission(models.Model):
    STATUS_ASSIGNED = 'assigned'
    STATUS_COMPLETE = 'complete'
    STATUS_CHOICES = [
        (STATUS_ASSIGNED, 'Assigned'),
        (STATUS_COMPLETE, 'Complete'),
    ]

    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_ASSIGNED)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mission #{self.id} for cat {self.cat.name}"
    

    def all_targets_completed(self):
        from apps.targets.models import Target
        return all(
            target.status == Target.STATUS_COMPLETE 
            for target in self.targets.all()
        )

