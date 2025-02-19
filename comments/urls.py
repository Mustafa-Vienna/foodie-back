from django.urls import path
from comments import views

app_name = 'comments'

urlpatterns = [
    path('', views.CommentList.as_view(), name='comments-list-create'),
    path('<int:pk>/', views.CommentDetailView.as_view(), name='comments-detail'),
]
