import json
import os

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

secret = json.loads(open(os.path.join(BASE_DIR, 'secret.json')).read())

SECRET_KEY = secret['SECRET_KEY']
ALLOWED_HOSTS = secret['ALLOWED_HOSTS']
DEBUG = secret['DEBUG']
DATABASES = secret['DATABASES']
ADMIN_URL = secret['ADMIN_URL']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

INSTALLED_APPS += [
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

'''
INSTALLED_APPS += [
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.line',
    'allauth.socialaccount.providers.linkedin',
]
'''

INSTALLED_APPS += [
    'sandbox',
    'quest',
    'job',
    'member',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'conf', 'templates'), ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}, ]

WSGI_APPLICATION = 'conf.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'th-TH'
LANGUAGES = [
    ('th', _('Thai')),
    ('en', _('English')),
]
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = 'UTC'

STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'conf', 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

SITE_ID = 1
