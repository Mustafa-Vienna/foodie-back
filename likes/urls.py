from django.urls import path
from likes import views

app_name = 'likes'

urlpatterns = [
    path('', views.LikeListCreateView.as_view(), name='like-list-create'),
    path('<int:pk>/', views.LikeDetailView.as_view(), name='like-detail'),
]
