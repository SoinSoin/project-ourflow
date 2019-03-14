from api.views import PageView
from django.urls import path, re_path, include

def all_pages():
    urlpatterns = [
        re_path(r'^page/', PageView.as_view()),
    ]
    return urlpatterns