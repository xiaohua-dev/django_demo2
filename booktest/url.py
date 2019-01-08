from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^create/$', views.create),
]
