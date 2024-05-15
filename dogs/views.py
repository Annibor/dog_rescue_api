from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dog
from .serializers import DogSerializer

# Create your views here.
class DogsListView(APIView):
  """
  List of all dogs available for adoption.
  """

  def get(self.request):
    dogs = Dog.objects.all()
    serializer = DogSerializer(dogs, many=True)
    return Response(serializer.data)