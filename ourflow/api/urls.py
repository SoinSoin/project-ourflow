from django.urls import path, re_path, include
from  api.url import all_pages

urlpatterns = [
    re_path(r'^page/', include(all_pages())),
]