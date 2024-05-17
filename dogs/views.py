from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from .models import Dog
from .serializers import DogsSerializer



# Create your views here.
class DogsListView(generics.ListAPIView):
  """
  List of all dogs available for adoption.
  Users can filter and search for dogs by their name, 
  breed and other attributes.
  """

  queryset = Dog.objects.all()
  serializer_class = DogsSerializer
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
  filterset_fields = ['name', 'breed', 'age', 'gender', 'good_with_children']
  search_fields = ['name', 'breed', 'age', 'gender', 'good_with_children']
  
    
class DogDetailView(APIView):
  """
  Retrieve the details of a single dog available for adoption.
  """
  def get(self, request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    serializer = DogsSerializer(dog)
    return Response(serializer.data)
