
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
# from sellers.views import *

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('users/signup',views.users_signup,name='users_signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

    # url(r'^mypage/(?P<pk>[0-9]+)/$',login_required(views.ProfileView.as_view()), name = 'mypage')
]
