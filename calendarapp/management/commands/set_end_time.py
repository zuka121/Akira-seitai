from django.core.management.base import BaseCommand
from calendarapp.models import Event
from datetime import timedelta

class Command(BaseCommand):
    help = 'Set default end_time for events'

    def handle(self, *args, **kwargs):
        events = Event.objects.filter(end_time__isnull=True)
        for event in events:
            event.end_time = event.start_time + timedelta(hours=1)
            event.save()
        self.stdout.write(self.style.SUCCESS('Successfully set end_time for events'))
