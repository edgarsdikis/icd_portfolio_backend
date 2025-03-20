import os
# Use a separate environment variable for determining which settings to load
django_env = os.environ.get('DJANGO_ENVIRONMENT', 'development')
if django_env == 'production':
    from .production import *
else:
    from .development import *
