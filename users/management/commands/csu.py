from django.core.management import BaseCommand

from message.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="alinadavydenko620@gmail.com")
        user.set_password("81726354")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
