from rest_framework import generics
from api.serializers import MailSerializer
from rest_framework.response import Response
from django.core.mail import send_mail

class SendMail(generics.views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = MailSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            name = validated_data.get('name')
            email =validated_data.get('email')
            phone = validated_data.get('phone')
            content =validated_data.get('content')
            try:
                send_mail("[CLIENT] mail de:{}".format(name),"Numéro de téléphone:{}.\nMessage:{}".format(phone, content) , email, ['contact@ourflow.fr'],)
                return Response({"response": "send"})
                pass
            except:
                return Response({'response': "failed"})
                pass
        return Response({'response': "failed"}, status=status.HTTP_400_BAD_REQUEST)



