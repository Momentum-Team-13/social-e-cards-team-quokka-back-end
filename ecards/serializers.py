from asyncio.format_helpers import _format_callback_source
from rest_framework import serializers
from .models import FollowRequest, User, Card


class UserSerializer(serializers.ModelSerializer):
    cards = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Card.objects.all())

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'cards',
        ]


class FollowSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField(source='user_id.id')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = FollowRequest
        fields = [
            'user',
            'following',
        ]


class FollowingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
        ]


class CardListSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.id')
    username = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = Card
        fields = (
            'id',
            'user_id',
            'username',
            'created_at',
            'title',
            'message',
            'font',
            'font_color',
            'bg_color',
            'border_color',
            'border_style',
            'img_src',
            )


class NewCardSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer(read_only=True)
    # this returns the entire user model nested in the card model

    user_id = serializers.ReadOnlyField(source='user_id.id')
    username = serializers.ReadOnlyField(source='user_id.username')
    # this returns only "user_id": id in the API
    # can change to user_id.username to return only the username if preferred

    class Meta:
        model = Card
        fields = (
            'id',
            'user_id',
            'username',
            'created_at',
            'title',
            'message',
            'font',
            'font_color',
            'bg_color',
            'border_color',
            'border_style',
            'img_src',
            )
