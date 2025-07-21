from django.urls import path, reverse_lazy
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, AddCommentView, DeleteCommentView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),  # Fix name
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
]

