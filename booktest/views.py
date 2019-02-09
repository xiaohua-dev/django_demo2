from django.shortcuts import render,redirect
from booktest.models import BookInfo
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template import loader,RequestContext
from datetime import date

# Create your views here.

# request就是httpRequest的请求对象

#登录装饰器
def login_required(view_func):
    def wrapper(request, *view_args, **view_kwargs):
        if request.session.has_key('isLogin'):
            return view_func(request, *view_args, **view_kwargs)
        else:
            return redirect('/login')

    return wrapper

@login_required
def index(request):
    books = BookInfo.objects.all()
    return render(request, 'booktest/index.html',{'books': books})

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
    if request.session.has_key('isLogin'):
        return redirect('/index')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ""
        return render(request, 'booktest/login.html',{'username': username})

def login_check(request):
    """登录视图校验"""
    # request.post 保存的是post方式提交的参数 QuerDict <class 'django.http.request.QueryDict'>
    # request.get 保存时get方式提交的参数
    # 1、获取提交的用户和密码
    username = request.POST.get("username")
    password = request.POST.get("password")
    remember = request.POST.get("remember")

    print(username)
    print(password)


    if username == 'xiao' and password == '123':
        response = redirect('/index')
        if remember == 'on':
            response.set_cookie('username', username, max_age=3600)

        request.session['isLogin'] = True
        return response

    else:
        return redirect('/login')

def ajax_test(request):
    '''暂时ajax页面'''
    return render(request, 'booktest/ajax_test.html')

def ajax_handle(request):
    '''处理ajax页面'''
    return JsonResponse({'res': 1})

def login_ajax(request):
    return render(request, 'booktest/login_ajax.html')

def login_ajax_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == 'xiao' and password == '123':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})


def set_cookie(request):
    response = HttpResponse('设置cookie')
    #设置一个cookie信息，名字为num，值为1
    response.set_cookie('num', 1, max_age=3600)
    return response


def get_cookie(request):
    #取出cookie值
    num = request.COOKIES['num']
    return HttpResponse(num)


def set_session(request):
    response = HttpResponse('设置session值')
    request.session['username'] = 'xiao'
    request.session['age'] = 22
    # session过期时间
    #request.session.set_expiry(5)

    return response

def get_session(request):
    username = request.session['username']
    age = request.session['age']

    return HttpResponse(username+":" + str(age))


def html_escape(request):
    return render(request, 'booktest/template_escape.html', {'content':'<h1>hello</h1>'})


@login_required
def change_pwd(request):
    return  render(request, 'booktest/change_pwd.html')




