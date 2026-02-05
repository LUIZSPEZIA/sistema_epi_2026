import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_epi_2026.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin123")
    print("Superusuário criado. - init.py:12")
else:
    print("Superusuário já existe. - init.py:14")
if not User.objects.filter(username="rh").exists():
    User.objects.create_superuser("rh", "rh@example.com", "rh123")
    print("Superusuário criado. - init.py:17")
else:
    print("Superusuário já existe. - init.py:19")

