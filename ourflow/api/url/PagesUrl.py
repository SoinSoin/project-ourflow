from api.views import PageView
from django.urls import path, re_path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

def all_pages():
    urlpatterns = [
        url(r'^', PageView.as_view()),
    ]
    return urlpatterns

# router = DefaultRouter()
# router.register(r'', PageViewSet.get_serializer_context, base_name='page')