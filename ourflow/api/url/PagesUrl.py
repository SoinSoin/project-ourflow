from api.views import AllPage, FilterNamePage, FilterNameTypePage
from django.urls import path, re_path, include

def page_url():
    urlpatterns = [
        re_path(r'^(?P<page>.+)/(?P<type>.+)/$', FilterNameTypePage.as_view()),
        re_path(r'^(?P<page>.+)/$', FilterNamePage.as_view()),
        re_path(r'^', AllPage.as_view()),
    ]
    return urlpatterns