from django.urls import path
from comments import views

app_name = 'comments'

urlpatterns = [
    path('comments/', views.CommentList.as_view(), name='comments-list-create'),
]
