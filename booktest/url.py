from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^create/$', views.create),
    url(r'^delete/(\d+)$', views.delete),
    url(r'^login/$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^test_ajax/$', views.ajax_test),
    url(r'ajax_handle/$', views.ajax_handle),

]
