from rest_framework import serializers
from api.models import ParaItem, Item
from .ItemsSerializer import ItemSerializer
import json
from rest_framework.response import Response

class ParaItemSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    class Meta:
        model = ParaItem
        fields = ('item',)
        depth=1

    def get_item(self, obj):
        context = self.context['request']
        qset = Item.objects.filter(id=obj.item_id)
        json_raw = [ItemSerializer(map_qset, context={'request':context}).data for map_qset in qset]
        parse_json_list = json.dumps(json_raw[0])
        parse_py = json.loads(parse_json_list)
        for key in parse_py: 
            if parse_py[key]==None:
                del json_raw[0][key]
        return json_raw[0]
