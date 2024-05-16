from django.urls import path
from account import views

urlpatterns = [
  path('account/', views.UserProfileView.as_view()),
  path('account/liked-dogs/', views.UserLikedDogsView.as_view(), name='liked-dogs'),
]