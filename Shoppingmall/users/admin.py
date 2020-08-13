from django.contrib import admin
from .models import *  #같은 경로의 models.py에서 User라는 클래스를 임포트한다.

# Register your models here.
#admin DB에 데이터 등록
admin.site.register(User)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'item','item_count')
    list_filter = ('user',)

admin.site.register(Like)

@admin.register(Buy)
class Buy(admin.ModelAdmin):
    list_display = ('user','item','item_count','price','buy_date','address','phone','price')
    list_filter = ('user','item')




