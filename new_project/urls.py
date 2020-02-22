
from django.contrib import admin
from django.urls import path,include
from . import views as home_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_views.index),
    # path('',include('app_name.urls'),name=''),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

