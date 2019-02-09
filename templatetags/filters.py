# 自定义过滤器
# 过滤器其实就是python函数

from django.template import library

register = library()

@register.filter
def mod(num):
    return num%2 == 0