from django.urls import path
from .views import ChannelDetailView, ChannelMessages, ChannelsView


urlpatterns = [
    path("", ChannelsView.as_view()),
    path("<int:id>/", ChannelDetailView.as_view()),
    path("<int:id>/messages/", ChannelMessages.as_view())
]