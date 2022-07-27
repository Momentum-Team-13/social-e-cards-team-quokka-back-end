# from django.shortcuts import render
from rest_framework import generics, permissions, renderers
# from rest_framework.reverse import reverse
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

from .models import User, Card
# from .permissions import
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    # allows creation of list of all User objects
    queryset = User.objects.all()
    serializer_class = UserSerializer
