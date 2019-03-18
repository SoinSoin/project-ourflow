from rest_framework import serializers
from api.models import ParaItem, Item
from .ItemsSerializer import ItemSerializer
from rest_framework.response import Response

class ParaItemSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    class Meta:
        model = ParaItem
        fields = ('item',)
        depth=1

    def get_item(self, obj):
        context = self.context['request']
        children = Item.objects.filter(id=obj.item_id)
        json_raw = ItemSerializer(children,  many=True, context={'request':context}).data
        return json_raw[0]
