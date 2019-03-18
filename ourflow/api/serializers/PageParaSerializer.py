from rest_framework import serializers
from api.models import PagePara,Paragraph
from .ParagraphsSerializer import ParagraphSerializer

class PageParaSerializer(serializers.ModelSerializer):
    paragraph = serializers.SerializerMethodField()
    class Meta:
        model = PagePara
        fields = ('paragraph',)
        depth=1
    def get_paragraph(self, obj, *args, **kwargs):
        context = self.context['request']
        qset = Paragraph.objects.filter(id=obj.paragraph_id)
        json_raw =[ ParagraphSerializer(m,  context={'request':context}).data for m in qset]
        return json_raw[0]