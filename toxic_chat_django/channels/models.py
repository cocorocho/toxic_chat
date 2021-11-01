from django.db import models
from accounts.models import User


class Channel(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name="members", blank=True)

    class Meta:
        verbose_name_plural = "Channels"

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey(Channel, on_delete=models.PROTECT, related_name="channel_messages")

    class Meta:
        verbose_name_plural = "Messages"
        ordering = ["-time"]

    def __repr__(self) -> str:
        return f"{self.author.username} ->>>> {self.channel.name}"

    def __str__(self) -> str:
        return f"{self.author.username} ->>>> {self.channel.name}"
        