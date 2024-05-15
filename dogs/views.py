from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dog
from .serializers import DogSerializer

# Create your views here.
class DogsListView(APIView):
  """
  List of all dogs available for adoption.
  """

  def get(self, request):
    dogs = Dog.objects.all()
    serializer = DogSerializer(dogs, many=True)
    return Response(serializer.data)
  
    
class DogDetailView(APIView):
  """
  Retrieve the details of a single dog available for adoption.
  """
  def get(self, request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    serializer = DogSerializer(dog)
    return Response(serializer.data)