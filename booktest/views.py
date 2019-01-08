from django.shortcuts import render
from booktest.models import BookInfo

# Create your views here.

def index(request):
    books = BookInfo.objest.all()

    return render(request,'booktest/index.html',{'books': books})