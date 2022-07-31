# from django.shortcuts import render
from django.shortcuts import get_object_or_404
# from requests import post
from rest_framework import generics, permissions, renderers, views
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Card, User
from .serializers import CardListSerializer, NewCardSerializer, UserSerializer
from ecards.permissions import IsOwner


@api_view(['GET'])
def welcome(request):
    return Response({
        'team': 'Team Quokka',
        'description': 'Back-end says heyyy 👋'
    })


class Profile(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        owner_queryset = self.queryset.filter(user_id=self.request.user)
        return owner_queryset
        # gets all card objects, then filters by user_id
        # returns queryset where user_id matches request of user


class FollowUser(views.APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user_id = request.data.get('user_id')
        user = get_object_or_404(User, id=user_id)
        request.user.follow(user)
        return Response(f'{self.user} followed')


class UserList(generics.ListAPIView):
    # allows creation of list of all User objects
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CardList(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer


class NewCard(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = NewCardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        # when a card instance is saved,
        # the user_id is the user that made the request


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer
