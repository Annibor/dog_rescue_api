from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileSerializer, AdoptionApplicationSerializer
from dogs.serializers import DogsSerializer
from rest_framework import status
from .models import UserProfile, AdoptionApplication
# Create your views here.

class UserProfileView(APIView):
  """
  Retrive or update a user's own profile information
  """

  serializer_class = UserProfileSerializer
  permission_classes = [IsAuthenticated]

  def get(self, request):
    """
    Retrive the UserProfile for the logged in user
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)

  
#  def put(self, request):
 #   """
#    Update the UserProfile for the logged in user
 #   """
#    user_profile = get_object_or_404(UserProfile, user=request.user)
#    serializer = UserProfileSerializer(user_profile, data=request.data)
 #   if serializer.is_valid():
 #     serializer.save()
#      return Response(serializer.data)
 #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLikedDogsView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    """
    Retrieve the list of dogs liked by the logged in user
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    liked_dogs = user_profile.liked_dogs.all()
    serializer = DogsSerializer(user_profile.liked_dogs, many=True)
    return Response(serializer.data)
  

class AdoptionApplicationListView(APIView):
  queryset = AdoptionApplication.objects.all()
  serializer_class = AdoptionApplicationSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    """
    Returns a list of all applications that the current user has submitted.
    """
    user = self.request.user
    return AdoptionApplication.objects.all.filter(user=user).order_by('created_at')
  
  
  