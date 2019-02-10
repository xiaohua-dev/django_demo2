from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^create/$', views.create),
    url(r'^delete/(\d+)$', views.delete),
    url(r'^login/$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^test_ajax/$', views.ajax_test),
    url(r'^ajax_handle/$', views.ajax_handle),
    url(r'^login_ajax/$', views.login_ajax),
    url(r'^login_ajax_check$', views.login_ajax_check),
    url(r'^set_cookie/$', views.set_cookie),
    url(r'^get_cookie/$', views.get_cookie),
    url(r'^set_session$', views.set_session),
    url(r'^get_session$', views.get_session),
    url(r'^html_escape/$', views.html_escape),
    url(r'^change_pwd/$', views.change_pwd),
    url(r'^verify_code/$', views.verify_code),
    url(r'^url_reverse/$', views.url_reverse),

]
