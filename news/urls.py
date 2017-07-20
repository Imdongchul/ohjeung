from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)?$', views.news_list , name="news_list"),
]