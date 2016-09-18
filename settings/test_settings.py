from .development import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ":memory:",
    }
}

#because of the 404 redirection
DEBUG=False

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
