from django.contrib import admin
from django.urls import include, path
from core import urls

urlpatterns = [
    path('admin/', admin.site.urls),
]
