
from django.urls import path
from . import views

# name : views의 해당 함수를 html 파일에서 name으로 호출할 수 있음 


urlpatterns = [

    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('users/signup',views.users_signup,name='users_signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('mypage/', views.mypage, name='usermypage'),

    path('category/<str:category>',views.category,name='category'),
    path('category/<str:category>/<str:product>',views.product,name='userproduct'),
    path('notice/', views.notice, name='usernotice'),
    path('notice/<int:pk>', views.noticedetail, name='usernotice_detail'),

    path('order_form/<str:product>', views.order_form, name='order_form'),
    path('purchase/', views.purchase, name='purchase'),
    path('cart/',views.cart, name='cart'),


]
