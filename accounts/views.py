# coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse  

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

from .forms import AccountLoginForm, AccountRegisterForm

from zeus.api import *

# Create your views here.

@defend_attack
def login_view(request):
    if request.method == 'POST':
        form = AccountLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"] 
            password = form.cleaned_data["password"] 
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    # User is valid, active and authenticated
                    messages.success(request, '登陆成功')
                    request.session.set_expiry(60*60*24)
                    login(request,user)
                    return redirect('dashboard_index')
                else:
                    # The password is valid, but the account has been disabled! 
                    messages.warning(request, '账号已锁,请联系管理员')
            else:
                # The username and password were incorrect
                messages.warning(request, '账号或密码不正确')
        else:
            messages.warning(request, '表单无效')
        return render_to_response("accounts/login.html", { 'form' : form }, context_instance=RequestContext(request))
    form = AccountLoginForm()
    return render_to_response("accounts/login.html", { 'form' : form }, context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('home_index')

def register(request):
    if request.user.is_authenticated():
         return redirect('home_index')

    if request.method == 'POST':
        form = AccountRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"] 
            password_confirm = form.cleaned_data["password_confirm"]
            if password == password_confirm:
                user = User.objects.filter(username=username)
                if len(user) > 0:
                    messages.warning(request, '用户已经存在') 
                else:
                    new_user = User()
                    new_user.username = username
                    new_user.password = make_password(password) 
                    new_user.is_active = False
                    new_user.is_staff = False
                    new_user.save()
                   
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        if user.is_active:
                            # User is valid, active and authenticated
                            messages.success(request, '用户创建成功,请登录')
                            login(request,user)
                            return redirect('accounts_login')
                        else:
                            # The password is valid, but the account has been disabled!
                            messages.warning(request, '账号已锁,请联系管理员')
                            return redirect('accounts_login')
                    else:
                        # The username and password were incorrect
                        messages.warning(request, '账号或密码不正确')
                
            else:
                messages.warning(request, '两次输入的密码不正确')            
        else:
            messages.warning(request, '表单无效')
    form = AccountRegisterForm() 
    return render_to_response("accounts/register.html",{ 'form' : form }, context_instance=RequestContext(request))
