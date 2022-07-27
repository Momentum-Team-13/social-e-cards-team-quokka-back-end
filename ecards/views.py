from rest_framework import generics
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User, Card
from .serializers import CardListSerializer, NewCardSerializer

# Create your views here.

class cardlist(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer

class new_card(CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = NewCardSerializer

class carddetail(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer