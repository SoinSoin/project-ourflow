from rest_framework import generics
from api.serializers import PageSerializer
from api.serializers import ItemSerializer
from api.models import Page, Item
from rest_framework.response import Response
from rest_framework import status, viewsets
class PageView(generics.ListAPIView):

    def get(self, request):
        queryset = Page.objects.all()
        serializer = PageSerializer(queryset, many=True, context={'request': request})
        return Response({'pages': serializer.data})
