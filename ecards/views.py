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

from .models import Card, User, Follow
from .serializers import CardListSerializer, NewCardSerializer, UserSerializer, FollowSerializer, FollowingListSerializer
from ecards.permissions import IsOwner, IsOwnerOrReadOnly


@api_view(['GET'])
def welcome(request):
    return Response({
        'team': 'Team Quokka',
        'description': 'Back-end says heyyy 👋'
    })


'''
Create, Update, Destroy API Views
'''


# allows creation of Follow object
class FollowUser(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # when a Follow instance is saved,
        # the user is the user that made the request


# allows creation of Card object
class NewCard(CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = NewCardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        # when a card instance is saved,
        # the user_id is the user that made the request


# allows GET
class CardDetail(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class UnfollowUser(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())
        following_pk = self.kwargs
        instance_of_follow_id = Follow.objects.filter(user=self.request.user, following=following_pk['pk']).first().id
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


'''
List API Views
'''


# returns list of all cards created
class CardList(ListAPIView):
    queryset = Card.objects.all().order_by("-created_at")
    serializer_class = CardListSerializer


# returns list of all cards by users being followed
class CardTimeline(ListAPIView):
    serializer_class = CardListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Card.objects.none()
        following_list = Follow.objects.filter(user=self.request.user)
        for follow in following_list:
            following_cards = Card.objects.filter(user_id=follow.following)
            queryset = queryset | following_cards
        return queryset.order_by("-created_at")


# returns list of all cards created by the user
class Profile(ListAPIView):
    queryset = Card.objects.all().order_by("created_at")
    serializer_class = CardListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        owner_queryset = self.queryset.filter(user_id=self.request.user)
        return owner_queryset
        # filter objects where user_id is user making request
        # return queryset of objects owned by user making request


# returns list of users being followed
class FollowingList(ListAPIView):
    serializer_class = FollowingListSerializer
    # queryset = Follow.objects.filter(user=request.user)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        # filter objects where user is user making request
        return queryset


class FollowerList(ListAPIView):
    serializer_class = FollowingListSerializer
    # permission_classes = [IsAuthenticated]

    # need to filter to show only users that self is following
    def get_queryset(self):
        following = self.request.user
        queryset = Follow.objects.filter(following=following)
        return queryset


class UserList(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all().order_by("username")
        # establish queryset of all User objects ordered by username
        search_term = self.request.query_params.get("username")
        # establishes variable to get query params
        # "search" key is "username"
        # if no keys match, will return None
        if search_term is not None:
            # filter using the search term
            queryset = User.objects.filter(username__icontains=search_term).order_by("username")
        return queryset

