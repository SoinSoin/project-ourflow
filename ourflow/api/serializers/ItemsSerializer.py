from rest_framework import serializers
from api.models import Item

class ItemSerializer(serializers.ModelSerializer):
    media_item = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ('title_item', 'descritpion_item', 'link_item', 'alt_item','media_item',)
     
    def get_media_item(self, obj):
        request = self.context['request']
        if obj.media_item:
            # obj.media_item.url.replace('/public', '/static/media')
            return "{0}://{1}/static/media/{2}".format(request.scheme, request.get_host(), obj.media_item.url)




        