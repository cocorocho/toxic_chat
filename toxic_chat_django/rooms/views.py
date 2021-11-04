from django.shortcuts import render
from rest_framework import permissions, serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.serializers import UserSerializer
from .serializers import ChannelSerializer, MessageSerializer
from .models import Channel, Message
from .serializers import MemberSerializer
from django.db import IntegrityError


class ChannelsView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request) -> Response:
        data = {}
        user = request.user
        members_of = user.members.all()
        channel_serializer = MemberSerializer(members_of, many=True)
        data["channels"] = channel_serializer.data
        return Response(data=data, status=HTTP_200_OK)

    def post(self, request) -> Response:
        user = request.user
        name = request.data["channel_name"]
        data = {}
        try:

            c = Channel.objects.create(
                name=name,
                owner=user,
            )
            c.save()
        except IntegrityError as e:
            data["message"] = "Channel already exists"
            return Response(status=HTTP_400_BAD_REQUEST, data=data)
        return Response(status=HTTP_201_CREATED, data=data)


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
        data = {
            "author": request.user.id,
            "content": request.data["message"],
            "channel": id
        }
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
        