from django.test import TestCase, Client
from accounts.models import User
from .models import Channel, Message


class TestChannels(TestCase):
    def setUp(self):
        self.owner_user = User.objects.create(username="supermario")
        self.owner_user.save()

    def test_channel_owner_is_member(self):
        channel = Channel.objects.create(name="SomeChannel", owner=self.owner_user)
        self.assertTrue(self.owner_user in channel.members.all())

    
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
                self.channel.message_set.get(content=word), word
            )