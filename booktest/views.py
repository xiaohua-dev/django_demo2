from django.shortcuts import render,redirect
from booktest.models import BookInfo
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from datetime import date

# Create your views here.

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