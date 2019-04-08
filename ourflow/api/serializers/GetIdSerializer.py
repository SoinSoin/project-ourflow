from rest_framework import serializers
from api.models import Item, Paragraph, Type, Page

class GetIdParagraph(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ('id',)

class GetIdPage(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id',)
    
class GetIdType(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id',)

class GetIdItem(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id',)