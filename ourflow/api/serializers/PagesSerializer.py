from rest_framework import serializers
from .PageParaSerializer import PageParaSerializer
from .ParagraphsSerializer import ParagraphSerializer
from api.models import PagePara 
from api.models import Page
# from .PageParaSerializer import PageParaSerializer

class PageSerializer(serializers.ModelSerializer):
    paragraph = serializers.SerializerMethodField()
    class Meta:
        model = Page
        fields = ('__all__')

    def get_paragraph(self, obj):
        qset = PagePara.objects.filter(page_id=obj)
        json_raw = [PageParaSerializer(m).data['paragraph'] for m in qset]
        return json_raw