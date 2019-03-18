from rest_framework import serializers
from api.models import Paragraph, Type, ParaItem
from .ParaItemsSerializer import ParaItemSerializer
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name_type',)

class ParagraphSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    item = serializers.SerializerMethodField()
    class Meta:
        model = Paragraph
        fields = ('title_para','item','type',)

    def get_type(self, obj):
        qset = Type.objects.filter(id=obj.type_id)
        json_raw = [TypeSerializer(m).data['name_type'] for m in qset]
        return json_raw[0]

    def get_item(self, obj):
        context = self.context['request']
        qset = ParaItem.objects.filter(paragraph_id=obj.id)
        json_raw =[ParaItemSerializer(m, context={'request':context}).data["item"] for m in qset]
        return json_raw