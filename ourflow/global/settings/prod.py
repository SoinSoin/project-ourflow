import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .base import *

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ['SECRET_KEY']

REST_FRAMEWORK = {'DEFAULT_RENDERER_CLASSES':('rest_framework.renderers.JSONRenderer',), 
'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication',)}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER_NAME'],
        'PASSWORD': os.environ['DB_USER_PSWD'],
        'HOST': 'localhost',
        'PORT': '5432',
    }   
}

MEDIA_URL = '/static/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "public/uploads")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'