from django.db import models
from django.utils.timezone import now
from datetime import timedelta

class Event(models.Model):
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)  # 一旦nullを許可
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
