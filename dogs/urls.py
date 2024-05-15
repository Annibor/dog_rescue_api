from django.urls import path
from dogs import views

urlpatterns = [
  path("dogs/", views.DogsListView.as_view()),
]