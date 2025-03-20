# production.py
from .base import *
import os
import dj_database_url

DEBUG = False

# Make sure to set these in environment variables on your hosting provider
SECRET_KEY = os.environ.get('SECRET_KEY')
MORALIS_API_KEY = os.environ.get('MORALIS_API_KEY')

# Update with your actual domain
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOST', 'your-production-domain.com')]

# Configure PostgreSQL using DATABASE_URL environment variable
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = 'DENY'

# CORS settings - restrict to your frontend domain
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    f"https://{os.environ.get('FRONTEND_DOMAIN', 'your-frontend-domain.com')}",
]
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    f"https://{os.environ.get('ALLOWED_HOST', 'your-production-domain.com')}",
    f"https://{os.environ.get('FRONTEND_DOMAIN', 'your-frontend-domain.com')}",
]

# Static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
