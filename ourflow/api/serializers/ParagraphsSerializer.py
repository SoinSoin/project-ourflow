from rest_framework import serializers
from api.models import Paragraph

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ('title_para','type',)