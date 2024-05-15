from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileSerializer
from rest_framework import status
from .models import UserProfile
# Create your views here.

class UserProfileView(APIView):
  """
  Retrive or update a user's own profile information
  """

  permission_classes = [IsAuthenticated]

  def get(self, request):
    """
    Retrive the UserProfile for the logged in user
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)

  
