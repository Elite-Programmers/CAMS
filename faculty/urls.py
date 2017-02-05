from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.facu,name='Faculty'),
    url(r'^student/$',views.student,name='Student'),
    url(r'^att/$',views.facu,name='Attendance'),
]
