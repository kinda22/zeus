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

def user_show(request):
    request.breadcrumbs([('Home', '/' ),('用户管理', reverse('manager_user_show'))])
    keyword = request.GET.get('keyword', '')
    page_peer = int(request.GET.get('page_peer', 5))
    page = int(request.GET.get('page', 1))

    if keyword:
        users = User.objects.filter(Q(username__icontains=keyword) | Q(first_name=keyword) | Q(last_name=keyword)).order_by('username')
    else:
        users = User.objects.all()

    user_list, page_range, page_peers = page_list(users,page_peer,page)
    return render_to_response("manager/user_show.html", locals(), context_instance=RequestContext(request))


@require_role(role='SA')
def user_add(request):
    request.breadcrumbs([('Home', '/' ),('新增用户', reverse('manager_user_show'))])

    if request.method == 'POST':
        form = UserFormAdd(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            password_confirm = form.cleaned_data["password_confirm"]

            fullname = form.cleaned_data["fullname"]
            gender = form.cleaned_data["gender"]
            tel = form.cleaned_data["tel"]
            mobile = form.cleaned_data["mobile"]
            address = form.cleaned_data["address"]
            QQ = form.cleaned_data["QQ"]
            position = form.cleaned_data["position"]
            native = form.cleaned_data["native"]

            is_active = form.cleaned_data["is_active"]

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
                    user = User.objects.create(username = username,password = make_password(password),is_active = not is_active,is_staff = False)
                    profile = UserProfile.objects.create(user = user, fullname = fullname, gender = gender, tel = tel, mobile = mobile,
                                                         address = address,QQ = QQ, position = position, native = native)



                except ServerError:
                     messages.warning(request, '用户创建失败')
                else:
                    messages.success(request, '用户创建成功')
                    return redirect('manager_user_show')

        else:
            messages.warning(request, '表单无效')
            return render_to_response("manager/user_add.html", locals(), context_instance=RequestContext(request))


    form = UserFormAdd()
    return render_to_response("manager/user_add.html", locals(), context_instance=RequestContext(request))




@require_role(role='SA')
def user_edit(request):
    request.breadcrumbs([('Home', '/' ),('编辑用户', reverse('manager_user_show'))])
    uid = request.GET.get('id')
    user_object = User.objects.get(pk=uid)
    userprofile_object = UserProfile.objects.filter(user__id = uid)

    if request.method == 'POST':
        form = UserFormEdit(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]

            fullname = form.cleaned_data["fullname"]
            gender = form.cleaned_data["gender"]
            tel = form.cleaned_data["tel"]
            mobile = form.cleaned_data["mobile"]
            address = form.cleaned_data["address"]
            QQ = form.cleaned_data["QQ"]
            position = form.cleaned_data["position"]
            native = form.cleaned_data["native"]

            is_active = form.cleaned_data["is_active"]

            try:
                user_object = user_object = User.objects.get(pk=uid)
                user_object.email = email
                user_object.save()
                if len(userprofile_object) > 0:
                    userprofile_object.update(fullname = fullname, gender = gender, tel = tel, mobile = mobile, address = address,QQ = QQ, position = position, native = native)
                else:
                    UserProfile.objects.create(user = user_object, fullname = fullname, gender = gender, tel = tel, mobile = mobile,address = address,QQ = QQ, position = position, native = native)

            except ServerError:
                messages.warning(request, '用户更新失败')
            else:
                messages.success(request, '用户更新成功')
                return redirect('manager_user_show')

        else:
            messages.warning(request, '表单无效')
            return render_to_response("manager/user_edit.html", locals(), context_instance=RequestContext(request))


    form = UserFormEdit(instance=user_object)
    return render_to_response("manager/user_edit.html", locals(), context_instance=RequestContext(request))

def user_del(request):
   return render_to_response("manager/user.html", { 'data': user }, context_instance=RequestContext(request))


def profile(request):
    request.breadcrumbs([('Home', '/' ),('个人设置', reverse('manager_profile'))])
    return render_to_response("manager/profile.html", context_instance=RequestContext(request))
