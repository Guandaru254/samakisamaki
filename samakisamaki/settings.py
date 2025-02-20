import os
from pathlib import Path

import dj_database_url
import environ

# Initialize the environment variables
env = environ.Env()
environ.Env.read_env()  # This loads the.env file into the environment

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Keep the secret key safe in production!
SECRET_KEY = os.getenv('SECRET_KEY')  # Use env variable

# Determine if the environment is development or production
DJANGO_DEVELOPMENT = os.getenv('DJANGO_DEVELOPMENT', 'False') == 'True'
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Allowed hosts and CSRF trusted origins
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost,samakisamaki.fly.dev').split(',')
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', 'http://localhost:8000,http://127.0.0.1:8000,https://samakisamaki.fly.dev').split(',')

# Security settings for cookies and HTTPS redirection
if DEBUG:
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False
    SECURE_SSL_REDIRECT = False
else:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True  # Always redirect to HTTPS in production
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

USE_X_FORWARDED_HOST = True  # Trust headers from reverse proxies (like Fly.io)

# Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'menu',
    'orders',
    'users',
    'reviews',
    'cart',
    'profiles',
    'checkout',
    'gallery',
    'payments',
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'samakisamaki.urls'

# Database configuration using dj-database-url
if DJANGO_DEVELOPMENT:
    # Use dj-database-url to parse the local DATABASE_URL (for local development)
    DATABASES = {
        "default": dj_database_url.config(
            default=os.getenv("DATABASE_URL", "postgres://postgres:%40Guandaru19@localhost:5432/postgres"),
            conn_max_age=600
        )
    }

else:
    # Production database configuration for Fly.io
    DATABASES = {
        "default": dj_database_url.config(
            default=os.getenv("PROD_DATABASE_URL"),  # use env variable
            conn_max_age=600,
            ssl_require=os.getenv("PROD_DB_SSL", "false").lower() == "true"
        )
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]

# Localization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files settings for production (WhiteNoise)
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
WHITENOISE_MAX_AGE = 31536000  # Cache static files for one year

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Login and logout redirects
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Secure session cookie settings
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 3600  # Set session expiration to 1 hour

# This header tells Django to trust the 'X-Forwarded-Proto' header from Fly.io
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Additional security settings
USE_X_FORWARDED_HOST = True  # Ensure headers are properly trusted from reverse proxies

# Caches (Optional for production)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # Local cache for development
    }
}

# Email settings (using environment variables)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = os.getenv('EMAIL_PORT', 587)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'your-email@gmail.com')  # Use env variable
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'your-password')  # Use env variable

# WhiteNoise - static file caching for production
WHITENOISE_MAX_AGE = 31536000  # Cache static files for one year

# TEMPLATES setting
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Ensure this points to the correct templates folder
        'APP_DIRS': True,  # This ensures app templates are found too
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]