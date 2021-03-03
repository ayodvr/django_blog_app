from django.urls import path
from . import views

urlpatterns = [
    path('register',views.UserCreateView.as_view(),name='register'),
    path('update_user/<int:pk>',views.UserUpdateView.as_view(),name='update_user'),
    path('user_detail/<int:pk>',views.UserDetailView.as_view(),name='user_detail'),
    path('profile',views.UserNewForm.as_view(),name='profile'),
    path('update_profile/<int:pk>',views.UserUpdateProfile.as_view(),name='update_profile'),
    path('delete_profile/<int:pk>',views.UserDeleteView.as_view(),name='delete_profile'),
]
