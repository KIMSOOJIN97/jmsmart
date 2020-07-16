
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('users/', include('users.urls')),
<<<<<<< HEAD
    path('sellers/', include('sellers.urls'))
=======
    path('sellers/', include('sellers.urls')),
>>>>>>> master

]
