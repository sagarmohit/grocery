from django.urls import path
from . import views

urlpatterns= [
    path('', views.index , name= 'index'),
    path('login', views.loginpage , name = 'login'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('addtodb', views.addtodb, name='addtodb'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('logout', views.userlogout, name='userlogout'),
    path('categoryselected', views.selectedcategory, name='selectedcategory'),
    path('addtocart', views.addtocart , name= 'addtocart'),
    path('cart', views.cart , name= 'cart'),
    path('deleteitem', views.deleteitem , name= 'deleteitem')
]