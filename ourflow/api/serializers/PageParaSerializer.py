from rest_framework import serializers
from api.models import PagePara,Paragraph, Type
from .ParagraphsSerializer import ParagraphSerializer, TypeSerializer
class PageParaSerializer(serializers.ModelSerializer):
    paragraph = serializers.SerializerMethodField()
    class Meta:
        model = PagePara
        fields = ('paragraph',)
        depth=1
    def get_paragraph(self, obj, *args, **kwargs):
        request = self.context['request']
        qset = Paragraph.objects.filter(id=obj.paragraph_id)
        json_raw = [ParagraphSerializer(m,  context={'request':request}).data for m in qset]
        del json_raw[0]["id"]
        return json_raw[0]