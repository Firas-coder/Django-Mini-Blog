from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts_search, name='all_posts_search'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('add_category/', views.add_category, name='add_category'),
]