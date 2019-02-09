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
    vcode = request.POST.get("vcode")
    vcode2 = request.session.get('verifycode')

    print(username)
    print(password)

    if vcode != vcode2:
        return  redirect('/login')
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




from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO

def verify_code(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    buf = BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')



