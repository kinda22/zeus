# coding: utf-8
from django.conf.urls import include, url
from .views import user_add, user_show, user_edit, profile

urlpatterns = [
    url(r'^user/$',    user_show,  name="manager_user_show"),
    url(r'^user/add$', user_add,   name="manager_user_add"),
    url(r'^user/edit$', user_edit,   name="manager_user_edit"),
    url(r'^user/del$', user_add,   name="manager_user_del"),
    url(r'^profile/$', profile,    name="manager_profile"),
]
