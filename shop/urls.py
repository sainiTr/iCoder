from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.index,name='ShopHome'),
    path('about',views.about ,name='aboutUs'),
    path('contact',views.contact,name='contactUs'),
    path('tracker',views.tracker,name='trackerStatus'),
    path('search',views.search,name='search'),
    path('productview/<int:id>',views.productview,name='productview'),
    path('uploadnew',views.UploadProd,name='checkout'),
    path('cart',views.checkcart,name='checkout'),
    path('productview',views.checkcart,name='checkout'),
    path('signup',views.SignUp,name='signup'),
    path('login',views.Login,name='signup'),
    path('profile',views.Profile,name='profile'),
    path('logout',views.logoutuser,name='logout'),
    path('checkoutprod/<str:cart>',views.checkoutproduct,name='checkoutprod'),
    path('ordernewupdate',views.pushorderupdate,name='pushorderupdate'),
    path('handlepayment',views.handlepayment,name='handle Payment'),
   
]
