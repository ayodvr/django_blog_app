from django.urls import path
from carApp import views

urlpatterns = [
    path('cars',views.cars,name='cars'),
    path('service',views.service,name='service'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('regform',views.students,name='regform'),
]