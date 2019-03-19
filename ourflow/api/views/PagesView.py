from rest_framework import generics
from api.serializers import PageSerializer, TypeSerializer, ParagraphSerializer
from api.models import Page,Type, Paragraph
from rest_framework.response import Response
from django.http import Http404

class PageView(generics.ListAPIView):
    serializer_class= PageSerializer
    def get_queryset(self):
        return Page.objects.all()

class PageFilterNameView(generics.ListAPIView):
    serializer_class= PageSerializer
    def get_queryset(self):
        page = self.kwargs['page'].replace("-"," ")
        return Page.objects.filter(title_page=page)

class PageFilterTypeNameView(generics.ListAPIView):
    serializer_class = PageSerializer
    def get_queryset(self):
        page = self.kwargs['page'].replace("-"," ")
        qtypes = self.kwargs['type'].replace("-"," ")
        if self.get_para_filter_type(qtypes=qtypes) != None:
            self.request.id_para = self.get_para_filter_type(qtypes=qtypes)
            return Page.objects.filter(title_page=page)

    def get_para_filter_type(self, qtypes):
        types = Type.objects.filter(name_type=qtypes).first()
        serialType = TypeSerializer(types).data
        queyset = Paragraph.objects.filter(type_id=serialType['id'])
        id_para_filter= [ParagraphSerializer(map_query,context={'request':self.request}).data['id'] for map_query in queyset]
        return id_para_filter
    

