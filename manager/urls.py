# coding: utf-8
from django.conf.urls import include, url
from .views import user_add, user_list, user_edit, user_del, user_show, group_list, group_add, profile

urlpatterns = [
    url(r'^user/$',     user_list,   name="manager_user_list"),
    url(r'^user/add$',  user_add,    name="manager_user_add"),
    url(r'^user/edit$', user_edit,   name="manager_user_edit"),
    url(r'^user/del$',  user_del,    name="manager_user_del"),
    url(r'^user/show$', user_show,   name="manager_user_show"),

    url(r'^group/$',    group_list,  name="manager_group_list"),
    url(r'^group/add$', group_add,   name="manager_group_add"),

    url(r'^profile/$',  profile,     name="manager_profile"),
]
