import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .base import *

ALLOWED_HOSTS = ['0.0.0.0']

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

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "public/uploads")

STATICFILES_DIRS += [MEDIA_ROOT]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
