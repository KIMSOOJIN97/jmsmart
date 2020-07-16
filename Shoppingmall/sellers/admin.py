from django.contrib import admin
<<<<<<< HEAD

from .models import Item

admin.site.register(Item)
=======
from .models import Seller   #같은 경로의 models.py에서 User라는 클래스를 임포트한다.

# Register your models here.
#admin DB에 데이터 등록
admin.site.register(Seller)

>>>>>>> master
