from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^secrets$', views.secrets),
    url(r'^popular$', views.popular),
    url(r'^process$', views.process),
    url(r'^users$', views.users),
    url(r'^delete/(?P<id>\d+)/(?P<sentby>\w+)$', views.newlike),
    url(r'^like/(?P<id>\d+)/(?P<sentby>\w+)$', views.newlike),
    url(r'^user/(?P<id>\d+)$', views.users),
]
