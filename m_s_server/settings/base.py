from datetime import timedelta
import os
from django.utils.translation import gettext_lazy as _
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '637a07d910d8330df9ed954d3a7934b9201b0c0b5900345f'
ALLOWED_HOSTS = ['messaging-system-server.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'm_s_server',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'm_s_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
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
WSGI_APPLICATION = 'm_s_server.wsgi.application'

CORS_ALLOW_HEADERS = (
    'app-version',
    'content-type',
    'authorization'
)

# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'm_s_server.utils.json_response_renderer.JsonResponseRenderer',
    )
}

JWT_AUTH = {
    'JWT_VERIFY_EXPIRATION': False,
    'JWT_EXPIRATION_DELTA': timedelta(days=7),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=30),
    'JWT_ALLOW_REFRESH': True
}

AUTH_USER_MODEL = 'm_s_server.User'

# INTERNATIONALIZATION
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', _('English'))
]

TIME_ZONE = 'Asia/Jerusalem'  # 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# STATIC FILES (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

APPEND_SLASH = False





