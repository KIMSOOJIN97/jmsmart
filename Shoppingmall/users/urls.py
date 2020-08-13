
from django.urls import path
from . import views

# name : views의 해당 함수를 html 파일에서 name으로 호출할 수 있음


urlpatterns = [

    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('users/signup', views.users_signup, name='users_signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('mypage/', views.mypage, name='usermypage'),


    path('category/<str:category>', views.category, name='category'),
    path('category/<str:category>/<str:product>',
         views.product, name='userproduct'),

    path('notice/', views.notice, name='usernotice'),
    path('notice/<int:pk>', views.noticedetail, name='usernotice_detail'),

    path('cart/', views.cart, name='cart'),
    path('purchase/list/', views.purchase, name='purchase'),


    path('category/<str:category>/<str:product>/order_form/<str:quantity>',
         views.only_order_form, name='only_order_form'),  # 상품상세에서 바로 구매하기 -->그상품만 결제
    path('order_form/<str:product>/<str:quantity>', views.order_form,
         name='order_form'),  # 장바구니에서 구매하기로넘어가기 (cartlist조회를 해서 선택한것들 구매)

]
