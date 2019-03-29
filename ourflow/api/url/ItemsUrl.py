from api.views import AllItem, FilterNameItem
from django.urls import path, re_path, include

def item_url():
    urlpatterns = [
        re_path(r'^(?P<item>.+)/$', FilterNameItem.as_view()),
        re_path(r'^', AllItem.as_view()),
    ]
    return urlpatterns