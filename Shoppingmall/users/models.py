from django.db import models
from sellers.models import *
from django.utils import timezone

# Create your models here.

class User(models.Model): #장고에서 제공하는 models.Model를 상속받아야한다.

    userID = models.CharField(max_length=64,verbose_name = '아이디')
    password = models.CharField(max_length=64,verbose_name = '비밀번호')
    username = models.CharField(max_length=64,verbose_name = '사용자명')
    postcode = models.CharField(max_length=64,verbose_name = '우편번호')
    address = models.CharField(max_length=64,verbose_name = '주소')
    detail_address = models.CharField(max_length=64,verbose_name = '상세주소')
    phone = models.CharField(max_length=64,verbose_name = '전화번호')
    e_mail = models.CharField(max_length=64,verbose_name = '이메일')
    
    #admin에서 테이블 이름 설정 
    def __str__(self):
        return self.userID

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_count = models.CharField(max_length=64, verbose_name="상품수")
    #
    # # admin에서 테이블 이름 설정
    # def __str__(self):
    #     return (self.user, self.item)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.user, self.item


class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_count = models.CharField( max_length=64,verbose_name="상품수")
    buy_date=models.DateTimeField(default=timezone.now,verbose_name="구매날짜")
    postcode=models.CharField(max_length=64,verbose_name = '우편번호')
    address = models.CharField(max_length=64,verbose_name = '주소')
    detail_address = models.CharField(max_length=64, verbose_name='상세주소')
    phone = models.CharField(max_length=64, verbose_name='전화번호')
    price = models.IntegerField(verbose_name = "주문가격")
    orderstate=models.CharField(max_length=64,default="주문완료")
    # delibary

