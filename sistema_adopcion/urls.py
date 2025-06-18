
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('adopcion.urls')),  
]

from django.contrib import admin
from django.urls import path, include
from adopcion.views import bienvenida  # 👈

urlpatterns = [
    path('', bienvenida),  # 👈
    path('admin/', admin.site.urls),
    path('', include('adopcion.urls')),
]
