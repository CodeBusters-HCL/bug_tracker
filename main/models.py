from django.db import models
from django.utils import timezone

# Create your models here.

severity_choices = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    ('critical', 'Critical'),
)

status = (
    ('assigned', 'Assigned'),
    ('unassigned', 'UnAssigned'),
    ('waiting_for_response', 'Waiting for Response'),
    ('dropped', 'Dropped'),
)
class Bug(models.Model):
    bug_category = models.CharField(max_length=200)
    bug_summary = models.TextField(max_length=200)
    bug_severity = models.CharField(max_length=8, choices=severity_choices, default='low')
    bug_desc = models.TextField(max_length=500)
    bug_status = models.CharField(max_length=20, choices=status, default='unassigned')
    date_reported = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.bug_summary


