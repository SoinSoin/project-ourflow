from rest_framework import serializers
from .PageParaSerializer import PageParaSerializer
from .ParagraphsSerializer import ParagraphSerializer
from api.models import PagePara, Page

class PageSerializer(serializers.ModelSerializer):
    paragraph = serializers.SerializerMethodField()
    class Meta:
        model = Page
        fields = ('title_page', 'link_to','paragraph',)

    def get_paragraph(self, obj):
        request=self.context['request']
        if hasattr(request,'id_para'):
            qset=[]
            for id_para in request.id_para:
                qset += PagePara.objects.filter(paragraph_id=id_para, page_id=obj.id)
        else: 
            qset = PagePara.objects.filter(page_id=obj.id)
        json_raw = [PageParaSerializer(m, context={'request': request}).data["paragraph"] for m in qset]
        return json_raw
