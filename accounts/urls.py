from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    # url(r'^$', views.joinus, name="joinus"),
    # url(r'^login/$', auth_views.login, name='login',
    # 	kwargs={'template_name': 'accounts/index_login_modal.html'}),
    url(r'^logout/$', auth_views.logout, name='logout',
    	kwargs={'next_page':views.index}),
   	url(r'^$', views.signup, name='signup'),
   	url(r'^profile/$', views.profile, name='profile'),
]