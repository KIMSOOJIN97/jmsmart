from django.contrib import admin
from .models import User   #같은 경로의 models.py에서 User라는 클래스를 임포트한다.

# Register your models here.
#admin DB에 데이터 등록
admin.site.register(User)

