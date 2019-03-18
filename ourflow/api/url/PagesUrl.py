from api.views import PageView,PageFilterNameView
from django.urls import path, re_path, include

def all_pages():
    urlpatterns = [
        re_path(r'^(?P<page>.+)/$', PageFilterNameView.as_view()),
        re_path(r'^', PageView.as_view()),
    ]
    return urlpatterns

# router = DefaultRouter()
# router.register(r'', PageViewSet.get_serializer_context, base_name='page')