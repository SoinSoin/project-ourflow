from rest_framework import generics
from api.serializers import MailSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
import re
class SendMail(generics.views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = MailSerializer(data=request.data)
        data_form = {"name" : request.data['name'],"email" :request.data['email'], "phone": request.data['phone'],"content" :request.data['content']}
        verify_data_form = verify_data(data_form=data_form)
        if(verify_data_form["isOk"]):
            if serializer.is_valid():
                validated_data = serializer.validated_data
                name = validated_data.get('name')
                email =validated_data.get('email')
                phone = validated_data.get('phone')
                content =validated_data.get('content')
                # send_mail("[FORM SITE] mail de:{}".format(name),"Numéro de téléphone:{}.\nMessage:{}".format(phone, content) , email, ['contact@ourflow.fr'],)
            else:
                verify_data_form["msg"]={"msg":"une erreur est survenue"}
                verify_data_form['status'] = status.HTTP_400_BAD_REQUEST
        return Response(verify_data_form["msg"], status=verify_data_form['status'] )

def verify_data(data_form,*args, **kwargs):
    is_ready_to_send = False
    if re.match(r"\S", data_form["name"]):
        if re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", data_form["email"]):
            if re.match(r"\S", data_form["phone"])  and True in [len(data_form["phone"])==val for val in [0,10]] and data_form["phone"].isdigit() or len(data_form["phone"])==0:
                if re.match(r"\S", data_form["content"]):
                    msg= {"msg": "send"}
                    real_status =status.HTTP_200_OK
                    is_ready_to_send = True
                else:
                    real_status = status.HTTP_400_BAD_REQUEST
                    msg={"msg": "Votre message n'est pas renseigné.", "from": "message"}
            else:
                real_status = status.HTTP_400_BAD_REQUEST
                msg = {"msg": "Votre numéro de téléphone n'est pas au format téléphone.","from": "phone"}
        else:
            real_status = status.HTTP_400_BAD_REQUEST
            msg = {"msg":"Votre mail n'est pas renseigné ou n'est pas au format mail.","from": "mail"}
    else:
        real_status = status.HTTP_400_BAD_REQUEST
        msg = {"msg": "Votre nom ou celui de votre entreprise n'est pas renseigné.", "from":"name"}
    return {"isOk": is_ready_to_send, "msg": msg, 'status':real_status}

