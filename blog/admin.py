from django.contrib import admin
from blog.models import Topblog,Comments
# admin.site.register(Blogpost)
admin.site.register((Topblog,Comments))