from django.contrib import admin
from django.urls import include, path
from core import urls, views

urlpatterns = [
    path('admin/', admin.site.urls),

]
