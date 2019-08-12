from django.utils.translation import ugettext_lazy as _

from .base import *

DEBUG = True

# Internationalization
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

# Static files (CSS, Javascript, Images)
STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'conf', 'static'),
    os.path.join(BASE_DIR, 'member', 'static'),
]

# Media files (Uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Error report
ADMINS = [('devteam', 'dev@pincoin.co.kr'), ]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'conf': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'job': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'member': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'quest': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'sandbox': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

'''
SESSION_COOKIE_SECURE = True
CSRF_USE_SESSIONS=False
CSRF_COOKIE_HTTPONLY=False
CSRF_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 15 * 60
SESSION_COOKIE_DOMAIN = '.codingjump.com'

FILE_UPLOAD_PERMISSIONS = 0o644
UPLOAD_FILE_MAX_SIZE = 8388608

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'
'''
