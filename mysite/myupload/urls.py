# this file was added by user, not created by manage.py

from django.conf.urls import url
from . import views

app_name='myupload'

urlpatterns = [
    url( r'^$', views.index, name='index'),
    url( r'^index', views.index, name='index'),
    url( r'^list',  views.list, name='list'),
    url( r'^(?P<file_id>[0-9]+)/detail/', views.detail, name='detail' ),
    url( r'^test/(?P<something>[a-z0-9]+)', views.test, name='test' ),
    url( r'^upload_file', views.upload_file, name='upload_file' ),
]
