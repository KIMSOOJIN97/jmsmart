from django.urls import path
from . import views

urlpatterns = [
    path('', views.item,name='item'),
    #views.index로 연결!
    path('register/',views.register,name='register')
]
