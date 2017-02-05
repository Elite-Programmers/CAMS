from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.ctea,name='ClassTeacher'),
    url(r'^faculty/$',views.faculty,name='Faculty'),
    url(r'^student/$',views.student,name='Student'),
    url(r'^att/$',views.ctea,name='Attendance'),
]
