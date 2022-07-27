from rest_framework import serializers
from .models import User, Card


class UserSerializer(serializers.ModelSerializer):
    cards = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Card.objects.all())

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'following',
        ]
