from django.core.management.base import BaseCommand, CommandError
from viz.data import create_data_point
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a new data point for your friend list.'

    def handle(self, *args, **options):
        user = User.objects.get(pk=1)
        create_data_point(user)
        self.stdout.write('Successfully created data point\n')