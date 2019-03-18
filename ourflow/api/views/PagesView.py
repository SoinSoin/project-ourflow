from rest_framework import generics
from api.serializers import PageSerializer
from api.models import Page,Paragraph
from rest_framework.response import Response

class PageView(generics.ListAPIView):
    def get(self, request):
        queryset = Page.objects.all()
        serializer = PageSerializer(queryset, many=True, context={'request': request})
        return Response({'pages': serializer.data})

class PageFilterNameView(generics.ListAPIView):
    serializer_class= PageSerializer
    def get_queryset(self):
        page = self.kwargs['page']
        return Page.objects.all().filter(title_page=page)
