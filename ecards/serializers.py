from asyncio.format_helpers import _format_callback_source
from rest_framework import serializers
from .models import Follow, User, Card


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
    user_id = serializers.ReadOnlyField(source='user.id')
    user_username = serializers.ReadOnlyField(source='user.username')
    following_id = serializers.ReadOnlyField(source='following.id')
    following_username = serializers.ReadOnlyField(source='following.username')

    class Meta:
        model = Follow
        fields = [
            'user_id',
            'user_username',
            'following_id',
            'following_username',
        ]


class FollowingListSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    user_username = serializers.ReadOnlyField(source='user.username')
    following_id = serializers.ReadOnlyField(source='following.id')
    following_username = serializers.ReadOnlyField(source='following.username')

    class Meta:
        model = Follow
        fields = [
            'id',
            'user_id',
            'user_username',
            'following_id',
            'following_username',
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
