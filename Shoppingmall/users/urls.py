
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('users/signup',views.users_signup,name='users_signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('category/<str:category>',views.category,name='category'),

    path('notice/', views.notice, name='usernotice'),
    path('notice/<int:pk>', views.noticedetail, name='usernotice_detail'),
    
    path('mypage/', views.mypage, name='usermypage'),
]
