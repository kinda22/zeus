# coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    request.breadcrumbs([('Home', '/' )])
    return render_to_response("home/index.html", context_instance=RequestContext(request)) 
