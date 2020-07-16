
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup',views.signup,name='sellers_signup'),
    path('sellers/notice/', views.NoticeListView.as_view(), name='notice'),
    path('sellers/notice/addPost', views.notice_addPost, name='notice_addPost'),
    path('sellers/notice/<int:pk>', views.NoticeDetailView.as_view(), name='notice_detail'),


    path('notice/',views.notice, name='usernotice'),
    path('notice/<int:pk>', views.noticedetail, name='usernotice_detail'),

]
