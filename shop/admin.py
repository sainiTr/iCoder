from django.contrib import admin
from .models import Product,User,orders,orderupdate

admin.site.register(Product)
admin.site.register(User)
admin.site.register(orders)
admin.site.register(orderupdate)

# Register your models here.
