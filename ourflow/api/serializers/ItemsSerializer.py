from rest_framework import serializers
from api.models import Item
from django.conf import settings

class ItemSerializer(serializers.ModelSerializer):
    media_item = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ('title_item', 'descritpion_item', 'link_item', 'alt_item','media_item',)
     
    def get_media_item(self, obj):
        request = self.context['request']
        if obj.media_item:
            if getattr(settings, "BASE_DIR", None):
                path_media = obj.media_item.url.replace("/media{}/public/uploads".format(getattr(settings, "BASE_DIR", None)), '')
                pass
            else:
                path_media = obj.media_item.url.replace("{}/public".format(getattr(settings, "BASE_DIR", None)), '')
                pass
            return "{0}://{1}{2}".format(request.scheme, request.get_host(),path_media)

        