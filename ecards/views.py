from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Card, Follow, User
from .permissions import IsOwnerOrReadOnly
from .serializers import CardListSerializer, NewCardSerializer, UserSerializer, FollowSerializer, FollowingListSerializer


'''
Root API View
'''


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
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # when a Follow object is saved,
        # the user is set as the user that made the request


# allows creation of Card object
class NewCard(CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = NewCardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        # when a Card object is saved,
        # the user_id is set as the user that made the request


# allows GET, PUT, PATCH, DELETE of Card object
class CardDetail(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    # requires user making request to own Card object
    # otherwise is ReadOnly access


# allows DELETE of Follow object
class UnfollowUser(DestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        following_pk = self.kwargs
        # establishes variable for kwarg dictionary
        instance_of_follow_id = Follow.objects.filter(user=self.request.user, following=following_pk['pk']).first().id
        breakpoint()
        # establishes variable to filter for Follow object id
        # of user-following relationship
        new_kwarg = {}
        # establishes variable for new kwarg
        new_kwarg['pk'] = instance_of_follow_id
        # inserts pk of user-following relationship to new kwarg dictionary
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in new_kwarg, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: new_kwarg[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

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
            # filter objects where user_id is following attribute ?
        return queryset.order_by("-created_at")


# returns list of all cards created by the user
class Profile(ListAPIView):
    queryset = Card.objects.all().order_by("created_at")
    serializer_class = CardListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.filter(user_id=self.request.user)
        # filter objects where user_id is user making request
        return queryset


# returns list of users being followed by the user making the request
class FollowingList(ListAPIView):
    serializer_class = FollowingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        # filter objects where user attribute is user making request
        return queryset


# returns list of users following the user making the request
class FollowerList(ListAPIView):
    serializer_class = FollowingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Follow.objects.filter(following=self.request.user)
        # filter objects where following attribute is user making request
        return queryset


# returns list of all users
class UserList(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all().order_by("username")
        # establish queryset of all User objects ordered by username
        search_term = self.request.query_params.get("username")
        # establishes variable to get query params by "search" key "username"
        # if no keys match, will return None
        if search_term is not None:
            queryset = User.objects.filter(username__icontains=search_term).order_by("username")
            # overrides queryset when search_term is present
            # filter objects where username contains search_term
        return queryset
