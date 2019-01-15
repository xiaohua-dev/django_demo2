from django.shortcuts import render,redirect
from booktest.models import BookInfo
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from datetime import date

# Create your views here.

# request就是httpRequest的请求对象

def index(request):
    books = BookInfo.objects.all()
    return render(request,'booktest/index.html',{'books': books})

def create(request):
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1992,1,2)
    b.save()

    return redirect('/index')
    #return HttpResponseRedirect('/index')

def delete(request, bid):
    #d = BookInfo.objects.filter(id=bid).delete()
    d = BookInfo.objects.get(id=bid)
    d.delete()
    return HttpResponseRedirect('/index')

def login(request):
    """登录视图"""
    return render(request, 'booktest/login.html')


def login_check(request):
    """登录视图校验"""
    # request.post 保存的是post方式提交的参数 QuerDict <class 'django.http.request.QueryDict'>
    # request.get 保存时get方式提交的参数
    # 1、获取提交的用户和密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == 'xiao' and password == '123':
        return redirect('/index')
    else:
        return redirect('/login')


