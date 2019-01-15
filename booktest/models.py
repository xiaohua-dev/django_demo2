from django.db import models

# Create your models here.


# class BookInfoManager(models.Manager):
#     '''图书模型管理类'''
#     def all(self):
#         # 1、改变查询结果集
#         books = super().all()
#         books = books.filter(isDelete=False)
#         return books
#
#     # 2、封装函数：操作模型类对应的数据表（增删数据表）
#     def create_book(self,btitle,bpub_date):
#         book = BookInfo()
#         book.btitle = btitle
#         book.bpub_date = bpub_date
#         book.save()
#         return book

class BookInfo(models.Model):
    btitle = models.CharField(max_length=30)
    # bprice = models.DecimalField(max_length=10,decimal_places=2)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)

    # @classmethod
    # def create_book(cls,btitle,bpub_date):
    #     obj = cls()
    #     obj.btitle = btitle
    #     obj.bpub_date = bpub_date
    #     obj.save()
    #     return obj

class HeroInfo(models.Model):
    hname = models.CharField(max_length=30)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=300)
    hbook = models.ForeignKey('BookInfo')
    isDelete = models.BooleanField(default=False)

# class NewsType(models.Model):
#     type_name = models.CharField(max_length=20)
#
#     #news_type = models.ManyToManyField('NewType')
#
# class NewsInfo(models.Model):
#     titile = models.CharField(max_length=128)
#     pub_date = models.DateField(auto_now_add=True)
#     content = models.TextField()
#     #关系属性，代表信息所属的类型;可以定义在两个其中一个中，即可（多对多的关系）
#     news_type = models.ManyToManyField('NewType')