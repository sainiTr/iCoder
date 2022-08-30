from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField
    name = models.CharField( max_length=100)
    category = models.CharField( max_length=50, default='')
    subcategory = models.CharField( max_length=50 ,default='')
    price = models.IntegerField(default=0)
    desc  = models.CharField( max_length=500)
    pubdate = models.DateField()
    image = models.ImageField(upload_to='shop/images',default='')
    
    available = models.IntegerField(default=0)

    def __str__(self):
        return self.name  

class User(models.Model):
    id = models.AutoField
    fname = models.CharField( max_length=20)
    lname = models.CharField( max_length=20)
    birthday = models.DateField(max_length=20)
    gender = models.CharField(max_length=6)
    email  = models.CharField( max_length=50)
    user = models.CharField(max_length=30,default='')
    image = models.ImageField(upload_to='shop/profiles',default='')
    passw = models.CharField(max_length=50)

    def __str__(self):
        return self.fname+" "+self.lname


class orders(models.Model):
    addr_id = models.AutoField(primary_key = True)
    cartjson = models.CharField(max_length=1000,default='')
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    amount = models.IntegerField(default=0)

    
class orderupdate(models.Model):
    id = models.AutoField(primary_key = True)
    up_id = models.CharField(max_length=10)
    desc = models.CharField(max_length=500)
    time  = models.DateField(auto_now_add=True)
