from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^callback/$', views.callback, name='auth_return'),
    url(r'^logout/$', views.unauth, name='oauth_unauth'),
    url(r'^auth/$', views.auth, name='oauth_auth'),
    url(r'^info/$', views.info, name='info'),
    url(r'^home_timeline/$',views.home_timeline, name='home_timeline'),
    url(r'^post_tweet/$',views.post_tweet, name='post_tweet'),
]