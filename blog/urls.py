from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    CreatePostView,
    UpdatePostView,
    DeletePostView
)

urlpatterns = [
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', UpdatePostView.as_view(), name='post_edit'),
    path('post/new/', CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]
