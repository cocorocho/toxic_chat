from django.shortcuts import render
from rest_framework import permissions, serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ChannelSerializer, MessageSerializer
from .models import Channel, Message
from .serializers import MemberSerializer


class ChannelsView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request) -> Response:
        data = {}
        user = request.user
        members_of = user.members.all()
        channel_serializer = MemberSerializer(members_of, many=True)
        data["channels"] = channel_serializer.data
        return Response(data=data, status=HTTP_200_OK)


class ChannelDetailView(APIView):
    # TODO ADD ISMEMBER PERM
    permission_classes = [IsAuthenticated, ]

    def get(self, request, id) -> Response:
        channel = Channel.objects.get(id=id)
        serializer = ChannelSerializer(channel)
        return Response(data=serializer.data, status=HTTP_200_OK)


class ChannelMessages(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, id) -> Response:
        channel = Channel.objects.get(id=id)
        serializer = ChannelSerializer(channel)
        messages = serializer.data["channel_messages"]
        return Response(data=messages, status=HTTP_200_OK)

    def post(self, request, id) -> Response:
        data = {}
        data["author"] = 1
        data["content"] = request.data["content"]
        message_serializer = MessageSerializer(data=data)
       
        return Response(status=HTTP_200_OK)