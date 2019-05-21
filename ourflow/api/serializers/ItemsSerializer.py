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
        base_url =  "{0}://{1}".format(request.scheme, request.get_host())
        if obj.media_item:
            if getattr(settings, "DEBUG", None):
                path_media = getattr(settings, "MEDIA_ROOT", None)
                pass
            else:
                path_media = getattr(settings, "STATIC_ROOT", None)
                pass
            with_media = "{0}{1}".format(base_url, obj.media_item.url.replace(path_media,""))
            return with_media.replace("/media","")
            pass
        else:
            return "null"
            pass