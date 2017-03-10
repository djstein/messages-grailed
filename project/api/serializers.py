from django.contrib.auth.models import User
from project.api.models import Channel, Message
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail")

    class Meta:
        model = User
        fields = ('url', 'id', 'username',)


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="channel-detail")
    messages = serializers.StringRelatedField(many=True, read_only=True)    

    class Meta:
        model = Channel
        fields = ('url', 'users', 'subject', 'messages')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="message-detail")
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Message
        fields = ('url', 'owner', 'channel', 'date', 'text')