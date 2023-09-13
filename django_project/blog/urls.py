from django.urls import path
from . import views
from .views import PostListView,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,CommentCreateView


urlpatterns = [
     # path('', views.home, name='blog-home'),
     path('', PostListView.as_view(), name='blog-home'),
     path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
     path('post/new/', PostCreateView.as_view(), name='post-create'),
     path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
     path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
     path('about/', views.about, name='blog-about'),
     path('like/<int:pk>/', views.LikeView, name='like_post'),
     path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_post'),
     
]

# Naming convention of class
