import os

environment = os.environ.get('DJANGO_SETTINGS_MODULE', 'backend.settings.development')

if environment == 'backend.settings.production':
    from .production import *
else:
    from .development import *
