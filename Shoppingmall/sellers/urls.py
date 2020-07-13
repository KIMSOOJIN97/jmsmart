
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='sellers_home'),
    path('signup',views.signup,name='sellers_signup'),
    path('login',views.login,name='sellers_login'),

]
