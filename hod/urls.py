from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.hod,name='HOD'),
    url(r'^classtchr/$', views.cltchr, name='classtchr'),
    url(r'^faculty/$', views.faculty, name='faculty'),
    url(r'^student/$', views.student, name='student'),
    url(r'^att/$',views.attn,name='Attendance'),
    url(r'^att2/$',views.student_list,name='Attendance2'),
]
