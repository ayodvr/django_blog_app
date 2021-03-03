from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view(),name='home'),
    path('list',views.SchoolList.as_view(),name='list'),
    path('detail/<int:pk>',views.SchoolDetail.as_view(),name='detail'),
    path('create',views.InsertRecs.as_view(),name='create'),
    path('update/<int:pk>',views.UpdateRecs.as_view(),name='update'),
    path('delete/<int:pk>',views.DeleteRecs.as_view(),name='delete'),
]   