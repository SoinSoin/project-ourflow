import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .base import *

ALLOWED_HOSTS = ['.ourflow.fr']

#cors header
CORS_ORIGIN_WHITELIST  = [
     "https://ourflow.fr",
]
CORS_ORIGIN_REGEX_WHITELIST  = [
    r"^https://\w+\.ourflow\.fr$",
]

CORS_ALLOW_METHODS  = [
     ' DELETE ' ,
     ' GET ' ,
     ' OPTIONS ' ,
     ' PATCH ' ,
     ' POST ' ,
     ' PUT ' ,
]

# CORS_ORIGIN_ALLOW_ALL = True

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

# Conf SMTP server
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= os.environ['MAIL_HOST']
EMAIL_HOST_USER= os.environ['MAIL_USER']
EMAIL_HOST_PASSWORD=os.environ['MAIL_PSWD']
EMAIL_PORT = 26
EMAIL_USE_TLS=True

MEDIA_URL = '/static/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "public/uploads")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'