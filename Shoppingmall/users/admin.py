from django.contrib import admin
from .models import *  #같은 경로의 models.py에서 User라는 클래스를 임포트한다.

# Register your models here.
#admin DB에 데이터 등록

# class ProfileInline(admin.StackedInline): # 로또 프로젝트에서 썼던 방식으로 유저 밑에 프로필 을 붙여서 보여주려고 이를 상속받음
#     model = Profile
#     con_delete = False                    # 프로필을 아예 없앨 수 없게 하는 속성(한번 만들면 지우는건 이상하니까)
#
#

admin.site.register(User)


