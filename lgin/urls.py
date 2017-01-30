from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='Login'),
    url(r'^authnt/$', views.lerror, name='Form'),
    url(r'^student/$',views.student,name='Student'),
    url(r'^admin/$',views.admn,name='Admin'),
    url(r'^hod/$',views.hod,name='HOD'),
    url(r'^faculty/$',views.facu,name='Faculty'),
    url(r'^cteacher/$',views.ctea,name='ClassTeacher'),
]
