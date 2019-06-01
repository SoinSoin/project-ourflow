import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .base import *

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ourflow_db',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Conf SMTP server
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= 'mail.ourflow.fr'
EMAIL_HOST_USER='contact@ourflow.fr'
EMAIL_HOST_PASSWORD='gehce7-hivhaq-peDger'
EMAIL_PORT = 26
EMAIL_USE_TLS=True

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "public/uploads")

STATICFILES_DIRS += [MEDIA_ROOT]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
