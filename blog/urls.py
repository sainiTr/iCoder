from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='BlogHome'),
    path('readblog_ID=<int:id>',views.blogview,name='BlogHome'),
    path('create-new-blog',views.newblog,name='newblog'),
    path('delete',views.delete,name='newblog'),
    path('postcomment',views.Postcomment,name='postcomment'),

]