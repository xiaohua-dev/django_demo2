from django.shortcuts import render
from booktest.models import BookInfo
from django.http import HttpResponse
from django.template import loader,RequestContext


# Create your views here.

def index(request):
    books = BookInfo.objects.all()
    return render(request,'booktest/index.html',{'books': books})