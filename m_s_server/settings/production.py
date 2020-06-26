from .base import *
import django_heroku

DEBUG = False
SERVE_MEDIA = False

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = (
    'app-version',
    'content-type',
    'authorization'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'messaging_system',
        'USER': 'messaging_system_admin',
        'PASSWORD': 'Aa123456',
        'HOST': 'localhost',
    }
}

# Activate Django-Heroku.
django_heroku.settings(locals())
