from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        def create_superuser(name, email, password):
            try:
                User.objects.create_superuser(name, f"{name}@example.com", name)
            except IntegrityError:
                print(f"{name} уже есть")

        create_superuser("admin1", "admin@example.com", "admin1")
        create_superuser("admin_cookies", "admin@example.com", "admin_cookies")
