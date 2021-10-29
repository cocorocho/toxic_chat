from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import UserSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_200_OK)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request) -> Response:
        data = {}
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token = Token.objects.get_or_create(user_id=user.id)[0]
            data["username"] = user.username
            data["token"] = token.key
            return Response(data=data, status=HTTP_200_OK)
        return Response(status=HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request) -> Response:
        request.user.auth_token.delete()
        return Response(status=HTTP_200_OK)
