# coding: utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.template import RequestContext

# Create your views here.

#@login_required
def index(request):
    request.breadcrumbs([('Home', '/' ),('仪表盘','/dashboard/')])
    return render_to_response('dashboard/index.html', context_instance=RequestContext(request))
