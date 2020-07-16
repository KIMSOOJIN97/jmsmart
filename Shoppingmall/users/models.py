from django.db import models

# Create your models here.

class User(models.Model): #장고에서 제공하는 models.Model를 상속받아야한다.
    
    userID = models.CharField(max_length=64,verbose_name = '아이디')
    password = models.CharField(max_length=64,verbose_name = '비밀번호')
    username = models.CharField(max_length=64,verbose_name = '사용자명')
    postcode = models.CharField(max_length=64,verbose_name = '우편번호')
    address = models.CharField(max_length=64,verbose_name = '주소')
    phone = models.CharField(max_length=64,verbose_name = '전화번호')
    e_mail = models.CharField(max_length=64,verbose_name = '이메일')


    def __str__(self):
        return self.userID

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)# 현 계정의 사용자를 가져올 수 있음.
#     nickname = models.TextField(max_length=10)
#     profile_photo = models.ImageField(blank=True)  # 값을 채워넣지 않아도 되는 속성.