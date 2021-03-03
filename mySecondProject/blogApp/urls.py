from django.urls import path
from . import views

urlpatterns = [
    path('draft_list',views.DraftListView.as_view(),name='draft_list'),
    path('create',views.PostCreateView.as_view(),name='create_post'),
    path('post_detail/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('publish/<int:pk>',views.publish_post,name='publish'),
    path('update_post/<int:pk>',views.PostUpdate.as_view(),name='update_post'),
    path('delete_post/<int:pk>',views.PostDelete.as_view(),name='delete_post'),
    path('comment/<int:pk>',views.AddCommentView.as_view(),name='comment'),
    path('covid19',views.CovidListView.as_view(),name='covid19'),
    path('prevention',views.PreventCovid.as_view(),name='prevention'),
    path('covid9ja',views.CovidNaija,name='covid9ja'),
]