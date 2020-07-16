<<<<<<< HEAD
=======

>>>>>>> master
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.item,name='item'),
    #views.index로 연결!
    path('register/',views.register,name='register')
=======
    path('',views.home,name='sellers_home'),
    path('signup',views.signup,name='sellers_signup'),
    path('login',views.login,name='sellers_login'),

>>>>>>> master
]
