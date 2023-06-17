from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

class Command(BaseCommand):
    def handle(self, *args, **options):
        def create_superuser(name, email, password):
            try:
                User.objects.create_superuser(name, f'{name}@example.com', name)
            except IntegrityError:
                print(f'{name} уже есть')
        create_superuser('admin', 'admin@example.com', 'admin')
        create_superuser('admin1', 'admin@example.com', 'admin1')
        create_superuser('admin_cookies', 'admin@example.com', 'admin_cookies')
        
