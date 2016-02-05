# coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.hashers import make_password

from zeus.api import *


from .forms import UserFormAdd, UserFormEdit
from .models import UserProfile

# Create your views here.


@require_role(role='SA')
def user_list(request):
    request.breadcrumbs([('Home', '/' ),('用户管理', reverse('manager_user_list'))])
    keyword = request.GET.get('keyword', '')
    page_peer = int(request.GET.get('page_peer', 5))
    page = int(request.GET.get('page', 1))

    if keyword:
        users = User.objects.filter(Q(username__icontains=keyword) | Q(first_name=keyword) | Q(last_name=keyword)).order_by('username')
    else:
        users = User.objects.all()

    user_list, page_range, page_peers = page_list(users,page_peer,page)
    return render_to_response("manager/user_list.html", locals(), context_instance=RequestContext(request))


@require_role(role='SA')
def user_show(request):
    request.breadcrumbs([('Home', '/' ),('编辑用户', reverse('manager_user_list'))])
    uid = request.GET.get('id')
    user = User.objects.get(pk=uid)
    if UserProfile.objects.filter(user=user).count() == 0:
        UserProfile.objects.create(user=user)

    return render_to_response("manager/user_show.html", locals(), context_instance=RequestContext(request))


@require_role(role='SP')
def user_add(request):
    request.breadcrumbs([('Home', '/' ),('用户管理', reverse('manager_user_list')),('新增用户', reverse('manager_user_list'))])

    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        fullname = request.POST.get("fullname")
        gender = request.POST.get("gender")
        tel = request.POST.get("tel")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        QQ = request.POST.get("QQ")
        position = request.POST.get("position")
        native = request.POST.get("native")

        is_active = request.POST.get("is_active",False)
        is_staff= request.POST.get("is_staff",False)

        try:
            if '' in [username, password, password_confirm]:
                messages.warning(request, '用户名和密码不能为空')
                raise ServerError

            if password != password_confirm:
                messages.warning(request, '两次输入的密码不正确')
                raise ServerError

            check_user_is_exist = User.objects.filter(username=username)
            if check_user_is_exist:
                messages.warning(request, '用户已经存在')
                raise ServerError

        except ServerError:
            return render_to_response("manager/user_add.html", locals(), context_instance=RequestContext(request))

        else:
            try:
                user = User.objects.create(username = username, password = make_password(password),is_active = is_active,is_staff = is_staff)
                profile = UserProfile.objects.create(user = user, fullname = fullname, gender = gender, tel = tel, mobile = mobile,
                                                         address = address,QQ = QQ, position = position, native = native)

            except ServerError:
                messages.warning(request, '用户创建失败')
            else:
                messages.success(request, '用户创建成功')
                return redirect('manager_user_list')


    return render_to_response("manager/user_add.html", locals(), context_instance=RequestContext(request))




@require_role(role='SP')
def user_edit(request):
    request.breadcrumbs([('Home', '/' ),('用户管理', reverse('manager_user_list')),('编辑用户', reverse('manager_user_list'))])
    uid = request.GET.get('id')
    user = User.objects.get(pk=uid)
    if UserProfile.objects.filter(user=user).count() == 0:
        UserProfile.objects.create(user=user)


    if request.method == 'POST':
        email = request.POST.get("email")
        fullname = request.POST.get("fullname")
        gender = request.POST.get("gender")
        tel = request.POST.get("tel")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        QQ = request.POST.get("QQ")
        position = request.POST.get("position")
        native = request.POST.get("native")

        is_active = request.POST.get("is_active")
        is_staff = request.POST.get("is_staff")


        try:
            user.email = email
            user.is_active = is_active
            user.is_staff = is_staff
            user.save()

            user.userprofile.fullname = fullname
            user.userprofile.gender = gender
            user.userprofile.tel = tel
            user.userprofile.mobile = mobile
            user.userprofile.address = address
            user.userprofile.QQ = QQ
            user.userprofile.position = position
            user.userprofile.native = native
            user.userprofile.save()
            
           
        except ServerError:
            messages.warning(request, '用户更新失败')
        else:
            messages.success(request, '用户更新成功')
            return redirect('manager_user_list')
   
    return render_to_response("manager/user_edit.html", locals(), context_instance=RequestContext(request))

@require_role(role='SP')
def user_del(request):
    uid = request.GET.get('id')
    User.objects.get(pk=uid).delete()
    messages.success(request, '用户删除成功')
    return redirect('manager_user_list')



def profile(request):
    request.breadcrumbs([('Home', '/' ),('个人设置', reverse('manager_profile'))])
    return render_to_response("manager/profile.html", context_instance=RequestContext(request))
