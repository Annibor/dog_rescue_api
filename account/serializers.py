from rest_framework import serializers
from .models import UserProfile, AdoptionApplication
from dogs.models import Dog


class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = "__all__"
    read_only_fields = ["user"]


class AdoptionApplicationSerializer(serializers.ModelSerializer):
  class Meta:
    model = AdoptionApplication
    fields = "__all__"
  
  def validate(self, data):
    """
    Ensure no active applications for the same dog by the same user.
    """
    if self.instance is None:
      active_status = ['pending', 'scheduled']
      existing_applications = AdoptionApplication.objects.filter(
        user= data['user'], dog= data['dog'], status__in=active_status
      )
      if existing_applications.exists():
        raise serializers.ValidationError("You have already applied for this dog.")
      return data