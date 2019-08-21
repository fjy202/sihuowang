"""
Definition of views.
"""

from django.shortcuts import render
from .models import *
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.models import User

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'主页',
            'ch1':'退出登录',
            'ch2':'登录',
            'ch3':'注册',
            'ch4':'特邀',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'联系',
            'message':'Your contact page.',
            'ch1':'退出登录',
            'ch2':'登录',
            'ch3':'注册',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'ch1':'退出登录',
            'ch2':'登录',
            'ch3':'注册',
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def signup(request,next_page):
    assert isinstance(request, HttpRequest)
    if request.method=="POST":
        obj=User.objects.create_user(username=request.POST.get("username"),password=request.POST.get("password"),last_login=None,is_superuser=False,first_name=request.POST.get("first_name"))
        obj.save()
        return HttpResponseRedirect(next_page)
    else:
        return render(
            request,
            'app/signup.html',
            {
                'title':'注册',
                'ch1':'退出登录',
                'year':datetime.now().year,
            }
        )
def invitations(request):
    objs=Invitation.objects
    print(objs.all())
    return render(
        request,
        "app/invitations.html",
        {
            'title':'我的特邀',
            'ch1':'退出登录',
            'ch2':'登录',
            'ch3':'注册',
            'objs':objs.all()
        })
def invita(request):
    if request.method=='POST':
        objs=Invitation.objects
        objs.create(fromuser=request.POST.get('email'),tousers=request.POST.get('tousers'),title=request.POST.get('title'),requires=request.POST.get('requires'))
        return HttpResponseRedirect('/')
    return render(
        request,
        "app/invita.html",
        {
            'title':'特邀',
            'ch1':'退出登录',
            'ch2':'登录',
            'ch3':'注册',
            'ch4':'目标',
            'ch5':'题目',
            'ch6':'需求'
        }
        )
def sihuo(request):
    objs=sihuo1.objects
    print(objs.all())
    return render(
        request,
        "app/sihuo.html",
        {
            'title':'私活',
            'ch1':'退出登录',
            'ch2':'登录',
            'ch3':'注册',
            'objs':objs.all()
        })
def tisihuo(request):
    if request.method=='POST':
        objs=sihuo1.objects
        objs.create(fromuser=request.POST.get('email'),title=request.POST.get('title'),requires=request.POST.get('requires'))
        return HttpResponseRedirect('/')
    return render(
        request,
        "app/tisihuo.html",
        {
            'title':'提私活',
            'ch1':'退出登录',
            'ch2':'登录',
            'ch3':'注册',
            'ch4':'目标',
            'ch5':'题目',
            'ch6':'需求'
        }
        )