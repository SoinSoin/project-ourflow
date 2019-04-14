from rest_framework import serializers

class  MailSerializer(serializers.Serializer):
    name = serializers.CharField();
    email = serializers.EmailField();
    phone = serializers.CharField(allow_blank=True,);
    content = serializers.CharField();