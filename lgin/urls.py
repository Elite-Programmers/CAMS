from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='Login'),
    url(r'^authnt/$', views.lerror, name='Form'),
    url(r'^admin/$', views.admn, name='Admin'),
]
