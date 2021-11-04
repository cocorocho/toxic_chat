from rest_framework import serializers
from .models import Message, Channel
from accounts.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)    

    class Meta:
        model = Message
        fields = ["author", "content", "time", "channel"]


class ChannelSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    members = UserSerializer(read_only=True, many=True)
    channel_messages = MessageSerializer(read_only=True, many=True)

    class Meta:
        model = Channel
        fields = ["name", "owner", "members", "channel_messages"]


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ["id", "name"]
