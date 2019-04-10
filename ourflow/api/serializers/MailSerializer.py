from rest_framework import serializers

class  MailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, min_length=0, allow_blank=False,);
    email = serializers.EmailField();
    phone = serializers.CharField(max_length=10, min_length=10, allow_blank=True,);
    content = serializers.CharField(allow_blank=False,);