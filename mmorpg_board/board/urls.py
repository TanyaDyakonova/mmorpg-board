from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    MyRepliesView, accept_reply, delete_reply
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('my-replies/', MyRepliesView.as_view(), name='my_replies'),
    path('reply/<int:reply_id>/accept/', accept_reply, name='accept_reply'),
    path('reply/<int:reply_id>/delete/', delete_reply, name='delete_reply'),
]
