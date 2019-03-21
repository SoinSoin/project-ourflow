from rest_framework import generics
from api.serializers import ItemSerializer, GetIdItem
from api.models import Item
from rest_framework.response import Response
from django.http import Http404

class AllItem(generics.ListAPIView):
    serializer_class= ItemSerializer
    def get_queryset(self):
        return Item.objects.all()

class FilterNameItem(generics.ListAPIView):
    serializer_class= ItemSerializer
    def get_queryset(self):
        qitem=self.kwargs['item'].replace("-"," ")
        qset =[]
        for id_item in self.get_filter_item(qitem=qitem):
            qset+=Item.objects.filter(id=id_item)
        return qset

    def get_filter_item(self, qitem):
        queyset = Item.objects.filter(title_item=qitem)
        id_item_filter= [GetIdItem(map_query,context={'request':self.request}).data['id'] for map_query in queyset]
        return id_item_filter