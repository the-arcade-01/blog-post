from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('',views.article_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail, name='detail'),
]
