
from django.urls import path
from . import views

urlpatterns = [
    path('',views.item,name='item'),
    path('signup',views.signup,name='sellers_signup'),
    path('login',views.login,name='sellers_login'),
    path('register/',views.register,name='register')

]
