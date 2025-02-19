from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListCreateView.as_view(), name='post-list-create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('tags/', views.TagListCreateView.as_view(), name='tag-list-create'),
]
