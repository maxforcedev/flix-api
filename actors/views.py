from rest_framework import generics
from actors.serializers import ActorSerializer
from actors.models import Actor

class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer