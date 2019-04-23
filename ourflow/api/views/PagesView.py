from rest_framework import generics
from api.serializers import PageSerializer, GetIdType, GetIdParagraph
from api.models import Page,Type, Paragraph
from rest_framework.response import Response

class AllPage(generics.ListAPIView):
    serializer_class= PageSerializer
    def get_queryset(self):
        return Page.objects.all()

class FilterNamePage(generics.ListAPIView):
    serializer_class= PageSerializer
    def get_queryset(self):
        page = self.kwargs['page'].replace("-"," ")
        return Page.objects.filter(title_page=page)

class FilterNameTypePage(generics.ListAPIView):
    serializer_class = PageSerializer
    def get_queryset(self):
        page = self.kwargs['page'].replace("-"," ")
        qtypes = self.kwargs['type'].replace("-"," ")
        self.request.id_para = self.get_para_filter_type(qtypes=qtypes)
        return Page.objects.filter(title_page=page)

    def get_para_filter_type(self, qtypes):
        types = Type.objects.filter(name_type=qtypes).first()
        serialType = GetIdType(types).data
        try:
            queyset = Paragraph.objects.filter(type_id=serialType['id'])
            id_para_filter= [GetIdParagraph(map_query,context={'request':self.request}).data['id'] for map_query in queyset]
            pass
        except :
            id_para_filter = [None]
            pass
        return id_para_filter
    

