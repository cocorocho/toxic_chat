from django.test import TestCase, Client
from accounts.models import User
from .models import Channel, Message
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


class TestChannels(TestCase):
    def setUp(self):
        self.owner_user = User.objects.create(username="supermario")
        self.owner_user.save()

    def test_channel_owner_is_member(self):
        channel = Channel.objects.create(name="SomeChannel", owner=self.owner_user)
        self.assertTrue(self.owner_user in channel.members.all())

    def test_create_channel(self):
        url = "/login/"
        client = Client()
        user = User.objects.create(username="janedoe")
        user.set_password("123456")
        user.save()
        data = {
            "username": "janedoe",
            "password": "123456"
        }
        response = client.post(url, data=data)
        user_token = Token.objects.get(user_id=user.id).key
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Token {user_token}")
        response = client.post("/channels/", data={"channel_name":"TestChannel"})
        self.assertIsInstance(
            Channel.objects.get(name="TestChannel"),
            Channel
        )

    
class TestMessages(TestCase):
    def setUp(self):
        self.channel_owner = User.objects.create(username="channelowner")
        self.channel_owner.save()
        self.random_user = User.objects.create(username="santa_claus")
        self.random_user.save()
        self.channel = Channel.objects.create(owner=self.channel_owner)
        self.channel.save()

    def test_send_message_to_channel(self):
        words = ["Hello", "How are you", "Who are you"]
        for word in words:
            msg = Message.objects.create(
                author=self.random_user,
                content=word,
                channel=self.channel
            )
            msg.save()
            self.assertTrue(
                self.channel.channel_messages.get(content=word), word
            )