from django.db import models
from django.utils import  timezone
from django.conf import settings
from django.urls import reverse

# Create your models here.

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

#공지사항 database
class Notice(models.Model):
    # author = models.ForeignKey(Seller,on_delete=models.CASCADE)
    title = models.CharField(verbose_name='제목',max_length=200)
    content = models.TextField(verbose_name='내용', default='')
    pub_date = models.DateTimeField(verbose_name='날짜',default= timezone.now)
    # view_count = models.DateTimeField

    # class Meta:
    #     verbose_name= 'notice'
    #     verbose_name_plural='notices'
    #     db_table='blog_notice'
    #     ordering = ('-mod_date')
    class Meta:
        ordering = ['-pub_date']
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice_detail', args=[str(self.id)])

    def get_absolute_url2(self):
        return reverse('usernotice_detail', args=[str(self.id)])




