from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('getallposts/', views.get_posts, name='get-all-posts'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('topic/<str:topic_name>', views.TopicListView.as_view(), name='topic-posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('search/', views.search, name='blog-search'),
    path('result/', views.result, name='blog-result'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]
