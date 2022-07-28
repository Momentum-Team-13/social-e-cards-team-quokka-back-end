# from django.shortcuts import render
from rest_framework import generics, permissions, renderers
# from rest_framework.reverse import reverse
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

from .models import User, Card
# from .permissions import
from .serializers import UserSerializer, CardListSerializer, NewCardSerializer


class UserList(generics.ListAPIView):
    # allows creation of list of all User objects
    queryset = User.objects.all()
    serializer_class = UserSerializer


class cardlist(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer


class new_card(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = NewCardSerializer


class carddetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer
