from django.db import models
from django.conf import settings

class Seller(models.Model): #장고에서 제공하는 models.Model를 상속받아야한다.
    
    sellerID = models.CharField(max_length=64,verbose_name = '아이디')
    password = models.CharField(max_length=64,verbose_name = '비밀번호')
    company_name = models.CharField(max_length=64,verbose_name = '회사명')
    postcode = models.CharField(max_length=64,verbose_name = '우편번호')
    address = models.CharField(max_length=64,verbose_name = '주소')
    phone = models.CharField(max_length=64,verbose_name = '전화번호')
    e_mail = models.CharField(max_length=64,verbose_name = '이메일')
    corporate_number = models.CharField(max_length=64,verbose_name = '사업자등록번호')

    def __str__(self):
        return self.sellerID



class Item(models.Model):
    name = models.CharField(max_length = 32, verbose_name="상품명")
    price = models.IntegerField(verbose_name = "상품가격",default=0)
    description = models.TextField(verbose_name="상품설명")
    stock = models.IntegerField(verbose_name="재고",default=1)
    image = models.ImageField(verbose_name="상품사진")
    detail_image = models.ImageField(verbose_name="상품상세사진")
  
    def __str__(self):
        return self.name

