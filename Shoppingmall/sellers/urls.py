
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup',views.signup,name='sellers_signup'),
    path('notice', views.notice , name='notice'),
    path('notice/<int:pk>/',views.notice, name='notice_detail'),
    path('notice/addPost', views.notice_addPost, name='notice_addPost'),

]
