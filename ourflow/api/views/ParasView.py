from rest_framework import generics
from api.serializers import GetIdType, ParagraphSerializer, GetIdParagraph
from api.models import Paragraph, Type
from rest_framework.response import Response
from django.http import Http404

class AllPara(generics.ListAPIView):
    serializer_class= ParagraphSerializer
    def get_queryset(self):
        return Paragraph.objects.all()

class FiterTypePara(generics.ListAPIView):
    serializer_class= ParagraphSerializer
    def get_queryset(self):
        qtypes=self.kwargs['type'].replace("-"," ")
        qset =[]
        for id_paras_type in self.get_para_filter_type(qtypes=qtypes):
            qset+=Paragraph.objects.filter(id=id_paras_type)
        return qset

    def get_para_filter_type(self, qtypes):
        types = Type.objects.filter(name_type=qtypes).first()
        serialType = GetIdType(types).data
        try:
            queyset = Paragraph.objects.filter(type_id=serialType['id'])
            id_para_filter= [GetIdParagraph(map_query,context={'request':self.request}).data["id"] for map_query in queyset]
        except:
            id_para_filter = [None]
        return id_para_filter

class FiterNamePara(generics.ListAPIView):
    serializer_class = ParagraphSerializer
    def get_queryset(self):
        qname=self.kwargs['para'].replace("-"," ")
        qset =[]
        for id_paras_name in self.get_para_filter_name(qname=qname):
            qset+=Paragraph.objects.filter(id=id_paras_name)
        return qset

    def get_para_filter_name(self, qname):
        try:
            queyset = Paragraph.objects.filter(title_para=qname)
            id_para_name= [GetIdParagraph(map_query,context={'request':self.request}).data['id'] for map_query in queyset]
        except:
            id_para_name=[None]
        return id_para_name
    

