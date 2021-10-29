from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data) -> User:
        user = User.objects.create(
            username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        Token.objects.create(user_id=user.id)
        return user
