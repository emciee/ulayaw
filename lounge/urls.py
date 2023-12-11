from django.urls import include, path
from core import urls
from . import views

urlpatterns = [
    path('', views.lounge, name='lounge'),
]
