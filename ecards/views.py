# from django.shortcuts import render
from csv import unregister_dialect
from django.shortcuts import get_object_or_404
from requests import request
# from requests import post
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Card, User, FollowRequest
from .serializers import CardListSerializer, NewCardSerializer, UserSerializer, FollowSerializer, FollowingListSerializer
from ecards.permissions import IsOwner, IsOwnerOrReadOnly


@api_view(['GET'])
def welcome(request):
    return Response({
        'team': 'Team Quokka',
        'description': 'Back-end says heyyy 👋'
    })


class Profile(ListAPIView):
    queryset = Card.objects.all().order_by("created_at")
    serializer_class = CardListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        owner_queryset = self.queryset.filter(user_id=self.request.user)
        return owner_queryset
        # gets all card objects, then filters by user_id
        # returns queryset where user_id matches request of user


class FollowUser(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FollowRequest.objects.all()
    serializer_class = FollowSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # when a followrequest instance is saved,
        # the user is the user that made the request


class UnfollowUser(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowSerializer
    queryset = FollowRequest.objects.all()

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())
        following_pk = self.kwargs
        instance_of_follow_id = FollowRequest.objects.filter(user=self.request.user, following=following_pk['pk']).first().id
        new_kwarg = {}
        new_kwarg['pk'] = instance_of_follow_id
        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in new_kwarg, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: new_kwarg[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj



class FollowingList(ListAPIView):
    serializer_class = FollowingListSerializer
    # user = self.request.user
    # queryset = FollowRequest.objects.filter(user=request.user)
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = FollowRequest.objects.filter(user=user)
        return queryset


class FollowerList(ListAPIView):
    serializer_class = FollowingListSerializer
    # permission_classes = [IsAuthenticated]

    # need to filter to show only users that self is following
    def get_queryset(self):
        following = self.request.user
        queryset = FollowRequest.objects.filter(following=following)
        return queryset

class UserList(ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        # we want this to work for requests that don't include a search term as well
        queryset = User.objects.all().order_by("username")
        # handle the case where we have query params that include a "search" key
        # if there are no search terms that match "search" this will be None
        search_term = self.request.query_params.get("username")
        if search_term is not None:
            # filter using the search term
            queryset = User.objects.filter(username__icontains=search_term).order_by("username")

        return queryset


class CardList(ListAPIView):
    queryset = Card.objects.all().order_by("-created_at")
    serializer_class = CardListSerializer


class NewCard(CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = NewCardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        # when a card instance is saved,
        # the user_id is the user that made the request


class CardDetail(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class CardTimeline(ListAPIView):
    serializer_class = CardListSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Card.objects.none()
        following_list = FollowRequest.objects.filter(user=self.request.user)
        for follow in following_list:
            following_cards = Card.objects.filter(user_id=follow.following)
            queryset = queryset | following_cards
        return queryset.order_by("-created_at")