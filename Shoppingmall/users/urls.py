
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('users/signup',views.users_signup,name='users_signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

]
