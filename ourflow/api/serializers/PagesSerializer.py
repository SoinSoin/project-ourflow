from rest_framework import serializers
from .PageParaSerializer import PageParaSerializer
from .ParagraphsSerializer import ParagraphSerializer
from api.models import PagePara, Page

class PageSerializer(serializers.ModelSerializer):
    paragraph = serializers.SerializerMethodField()
    class Meta:
        model = Page
        fields = ('title_page', 'link_to','paragraph', 'id',)

    def get_paragraph(self, obj):
        context=self.context['request']
        qset = PagePara.objects.filter(page_id=obj.id)
        json_raw = [PageParaSerializer(m, context={'request': context}).data["paragraph"] for m in qset]
        return json_raw
