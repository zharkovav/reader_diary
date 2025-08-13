import os
import sys
import django

# Add the project directory to the Python path
sys.path.append('d:/repo/reader_diary')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reader_diary.settings')

# Setup Django
django.setup()

# Create the superuser
from django.contrib.auth import get_user_model
User = get_user_model()

# Check if the user already exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print('Superuser created successfully!')
else:
    print('Superuser already exists!')