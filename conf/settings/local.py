from .base import *

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