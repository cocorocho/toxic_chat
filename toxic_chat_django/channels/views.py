from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ChannelSerializer, MessageSerializer
from .models import Channel, Message


class ChannelView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, channel_id):
        channel = Channel.objects.get(id=channel_id)
        messages = channel.messages_set.all()
