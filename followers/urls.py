from django.urls import path
from followers import views

app_name = 'followers'

urlpatterns = [
    path('followers/', views.FollowerListCreateView.as_view(), name='followers-list-create'),
    path('followers/<int:pk>/', views.FollowerDetailView.as_view(), name='followers-detail'),
]
