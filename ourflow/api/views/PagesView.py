from rest_framework import generics
from api.serializers import PageSerializer
from api.models import Page

class PageView(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
