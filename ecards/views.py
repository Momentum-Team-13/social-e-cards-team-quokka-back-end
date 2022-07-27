from rest_framework import generics
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User, Card
from .serializers import CardListSerializer

# Create your views here.

class cardlist(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer