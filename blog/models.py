from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
import datetime

# Create your models here.

# class Blogpost(models.Model):

#     titel = models.CharField(max_length=100,default='')
#     head0 = models.CharField( max_length=100,default='')
#     chead0 = models.TextField(max_length=1000,default='')
#     head1 = models.CharField( max_length=100,null=False,blank=True)
#     chead1 = models.TextField(max_length=1000,default='',blank=True,null=False)
#     head2 = models.CharField( max_length=100,null=False,blank=True)
#     chead2 = models.TextField(max_length=1000,default='',blank=True,null=False)
#     bdate = models.DateField(default=datetime.now())
#     image = models.ImageField(upload_to='blog/images',default='')
#     about = models.TextField(max_length=1000,default="",blank=True,null=False)
#     def __str__(self):
#         return self.titel

class Topblog(models.Model):
    title = models.CharField(max_length=200,blank=False,default='')
    content = models.TextField(blank=False)
    date = models.DateField(default=datetime.date.today())    
    auther = models.CharField(default='Tenali',max_length=50,blank=False)
    views = models.IntegerField(default=0)
    desc = models.TextField(blank=False,default='')
    def __str__(self):
        return self.title[0:50]

class Comments(models.Model):
    # sno = models.AutoField()
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Topblog,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    times =models.DateTimeField(default=now)
    auther  = models.CharField(max_length=50)
    icon = models.ImageField(upload_to= 'media/blog/ic  on',default='')
    
    def __str__(self):
        return 'comment =:   '+self.comment[:40]
    