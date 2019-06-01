import os
import sys
from whitenoise import WhiteNoise
# set variables
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'global.settings'
#setup django application
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
application = WhiteNoise(application)