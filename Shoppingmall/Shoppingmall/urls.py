
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 



from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views as views_ckeditor
from django.views.decorators.cache import never_cache


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('sellers/', include('sellers.urls')),

    path(r'^upload/', login_required(views_ckeditor.upload), name='ckeditor_upload'),
    path(r'^browse/', never_cache(login_required(views_ckeditor.browse)), name='ckeditor_browse'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)