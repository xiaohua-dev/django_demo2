from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=30)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    hname = models.CharField(max_length=30)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=300)
    hbook = models.ForeignKey('BookInfo')
    isDelete = models.BooleanField(default=False)
