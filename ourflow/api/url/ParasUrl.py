from api.views import AllPara, FiterTypePara, FiterNamePara
from django.urls import path, re_path, include

def para_url():
    urlpatterns = [
        re_path(r'^type/(?P<type>.+)/$', FiterTypePara.as_view()),
        re_path(r'^name/(?P<para>.+)/$', FiterNamePara.as_view()),
        re_path(r'^', AllPara.as_view()),
    ]
    return urlpatterns