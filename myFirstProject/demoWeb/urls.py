from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexx, name='index'),
    path('another', views.anotherMethod, name='another'),
]