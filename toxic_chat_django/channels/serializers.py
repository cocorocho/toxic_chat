from rest_framework import serializers
from .models import Message, Channel
from accounts.serializers import UserSerializer


class ChannelSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    members = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Channel
        exclude = ["id"]


class MessageSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)    
    channel = ChannelSerializer()

    class Meta:
        model = Message
        exclude = ["id", "time"]
