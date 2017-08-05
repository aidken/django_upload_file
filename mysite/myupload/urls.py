# this file was added by user, not created by manage.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url( r'^$', views.index, name='index'),
    url( r'^index', views.index, name='index'),
]
