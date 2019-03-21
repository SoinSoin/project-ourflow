from rest_framework import generics
from rest_framework.response import Response
from django.http import Http404

class InfoApi(generics.ListAPIView):

    def get(self, request):
        base_url = "{0}://{1}/api/".format(request.scheme, request.get_host())
        obj_info={
            "infos": "Bienvenu sur l'API OurFlow. Sur cette page vous trouverez les informations sur les routes",
            "api":{
                "base url":base_url,
                "base url dev": base_url+"?format=json",
                "routes":{
                    "page":{
                        "/page/" : "affiche toutes les pages avec tout son contenus",
                        "/page/<:title>/" : "affiche une page en fonction de son titre (mettre un tiret si le titre est composé)",
                        "/page/<:title>/<:type-paragrahe>/" : "affiche une page en fonction de son titre et du type de paragraphe (mettre un tiret si le titre et type du paragraph  est composé)",
                    },
                    "paragraph": {
                        "/paragraph/":"affiche tout les paragraph avec tout son contenus",
                        "/paragraph/type/<:type>/":"affiche tout les paragraph de même type (mettre un tiret si le type est composé)",
                        "/paragraph/type/<:para>/":"affiche un paragraph en fonction du nom (mettre un tiret si le nom est composé)",
                    },
                    "item": {
                        "/item/":"affiche tout les items avec tout son contenus",
                        "/paragraph/type/<:item>/":"affiche un item en fonction du nom (mettre un tiret si le nom est composé)",
                    }
                }
            }
        }
        return Response(obj_info)