from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.template import loader
from . import views
import markdown
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def index(request):
    template = loader.get_template("index.html")
    context={}
    return HttpResponse(template.render(context, request))

def login(request):
    template=loader.get_template('login.html')
    context={}
    return HttpResponse(template.render(context, request))

def login_check(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect('/edit')
    else:
        return HttpResponseForbidden()
    
@login_required(login_url="/login")
def edit(request):
    template = loader.get_template("edit.html")
    context ={}
    return HttpResponse(template.render(context, request))

def experienceView(request):
    experiences = Experience.objects.all() 
    template = loader.get_template("experience.html")
    context = {"exp": experiences}
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template("contact.html")
    context ={}
    return HttpResponse(template.render(context, request))