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
        context = self.context['request']
        types = Type.objects.filter(name_type=context.query_params['type'])
        # print(dir(types))
        print(types)
        qset = Paragraph.objects.filter(id=obj.paragraph_id)
        json_raw =[ ParagraphSerializer(m,  context={'request':context}).data for m in qset]
        return json_raw[0]