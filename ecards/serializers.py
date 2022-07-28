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


class CardListSerializer(serializers.ModelSerializer):
    # # Uncomment when User Serializer is merged with this
    # user_id = UserSerializer(read_only=True)

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
            'img_src'
            )


class NewCardSerializer(serializers.ModelSerializer):
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
            'img_src'
            )
