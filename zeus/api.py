# coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse

from django.forms.utils import ErrorList
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage


class BtnErrorList(ErrorList):
    '''
        .....
    '''
    def __unicode__(self):
        return self.as_btn()

    def as_btn(self):
        if not self: return ''
        return ''.join(['<button class="btn btn-warning tooltip-warning" data-toggle="tooltip" data-placement="top" data-original-title="Warning Tooltip">%s</button>' % e for e in self])


def defend_attack(func):
    '''
        登陆失败10次,禁止登陆300s 
    '''
    def _deco(request, *args, **kwargs):
        if int(request.session.get('visit', 1)) > 10:
            #logger.debug('请求次数: %s' % request.session.get('visit', 1))
            return HttpResponse('Forbidden', status=403)
        request.session['visit'] = request.session.get('visit', 1) + 1
        request.session.set_expiry(300)
        return func(request, *args, **kwargs)
    return _deco

def require_role(role='SA'):
    """
        要求用户是管理员或超级管理员
    """
    def _deco(func):
        def __deco(request, *args, **kwargs):
            if not request.user.is_authenticated():
                return HttpResponseRedirect(reverse('accounts_login'))

            if role == 'SA':
                if not request.user.is_staff:
                    return HttpResponseRedirect(reverse('index'))
            elif role == 'SP':
                if not request.user.is_superuser:
                    return HttpResponseRedirect(reverse('index'))
            return func(request, *args, **kwargs)

        return __deco

    return _deco


class ServerError(Exception):
    """
    self define exception
    自定义异常
    """
    pass


def page_list(content_list,page_peer=5,page=1):
    '''
        指定分页
    '''
    page_peers = [5,15,20,100]
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页

    paginator = Paginator(content_list, page_peer)
    try:
        contents = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        contents = paginator.page(paginator.num_pages)

    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]

    return (contents,page_range,page_peers)

