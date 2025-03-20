import os
# Use consistent environment variable name
django_settings = os.environ.get('DJANGO_SETTINGS_MODULE', 'backend.settings.development')
if django_settings.endswith('production'):
    from .production import *
else:
    from .development import *
