from django.urls import path, re_path, include
from api.views import InfoApi
from  api.url import * 

urlpatterns = [
    re_path(r'^page/', include(page_url())),
    re_path(r'^paragraph/', include(para_url())),
    re_path(r'^item/', include(item_url())),
    re_path(r'^', InfoApi.as_view()),
]