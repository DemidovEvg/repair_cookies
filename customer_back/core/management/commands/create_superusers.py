from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = get_user_model()
        for phone, name in enumerate(("admin", "admin1", "admin_cookies")):
            try:
                client.objects.create_superuser(
                    username=name,
                    email=f"{name}@example.com",
                    password=name,
                    phone_number=f"+7999999999{phone}",
                )
            except IntegrityError:
                pass
        print("🙌 Created 🥳")
