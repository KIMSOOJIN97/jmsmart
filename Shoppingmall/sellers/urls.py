
from django.urls import path
from . import views

urlpatterns = [
    path('',views.item,name='item'),
    path('signup',views.signup,name='sellers_signup'),
    path('login',views.login,name='sellers_login'),
    path('register/',views.register,name='register'),

    path('notice/',views.NoticeListView.as_view(), name='notice'),
    path('notice/addPost', views.notice_addPost, name='notice_addPost'),
    path('notice/<int:pk>', views.NoticeDetailView.as_view(), name='notice_detail'),


]
