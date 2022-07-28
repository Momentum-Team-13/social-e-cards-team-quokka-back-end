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
            'cards',
        ]


class CardListSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)

    class Meta:
        model = Card
        fields = (
            'id',
            'user_id',
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
    user_id = serializers.ReadOnlyField(source='user_id.id')
    # this returns "user_id": id in the API
    # we can cange to user_id.username to return the username if preferred
    # by including this line, the user of the card is auto set when created

    class Meta:
        model = Card
        fields = (
            'id',
            'user_id',
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
