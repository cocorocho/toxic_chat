from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Channel


@receiver(post_save, sender=Channel)
def add_owner_as_member(sender, instance, **kwargs):
    """
    Auto adds owner as member of a channel after channel creation.
    """
    if kwargs.get("created"):
        instance.members.add(instance.owner)