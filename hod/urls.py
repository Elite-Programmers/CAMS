from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.hod,name='HOD'),
    url(r'^classtchr/$', views.cltchr, name='classtchr'),
    url(r'^faculty/$', views.faculty, name='faculty'),
]
