from rest_framework import generics
from django.http import HttpResponse, Http404
from django.conf import settings
import os
import mimetypes

class  GetMedia(generics.views.APIView):
    def get(self, request, *args, **kwargs):
        FILE_DIR = request.path.replace('/static/media', '/public')
        FILE_ROOT= "{}{}".format(getattr(settings, "BASE_DIR", None), FILE_DIR)
        response=Http404( "not-found")
        try:
            fsock = open(FILE_ROOT, "rb")
            file_mime = mimetypes.guess_type(FILE_ROOT)
            response = HttpResponse(fsock, content_type=file_mime[0])
            return response
        except:
            return response