from typing import Any
from blog.models import Categorys
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "This commands inserts post data"

    def handle(self, *args: Any, **options: Any):

        Categorys.objects.all().delete()

        names = ['sports','arts','technology','science','food']

        for name in names:
            Categorys.objects.create(name = name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))