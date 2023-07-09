from customer.settings import PHONE_NUMBER_REGION
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from phonenumber_field.phonenumber import PhoneNumber


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = get_user_model()
        for phone, name in enumerate(("admin", "admin1", "admin_cookies")):
            number = PhoneNumber.from_string(f"8999999999{phone}", region=PHONE_NUMBER_REGION)
            try:
                client.objects.create_superuser(
                    username=name,
                    email=f"{name}@example.com",
                    password=name,
                    phone_number=number.as_e164,
                )
            except IntegrityError:
                pass
        print("🙌 Created 🥳")
