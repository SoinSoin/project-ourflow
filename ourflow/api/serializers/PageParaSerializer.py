from rest_framework import serializers
from api.models import PagePara
from .ParagraphsSerializer import ParagraphSerializer

class PageParaSerializer(serializers.ModelSerializer):
    paragraph = ParagraphSerializer()
    class Meta:
        model = PagePara
        fields = ('paragraph',)
        depth = 1