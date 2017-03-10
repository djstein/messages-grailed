from django.contrib.auth.models import User
from project.api.models import Channel, Message
from rest_framework import serializers
"""
Very similar to Django Form class
Use ModelSerializers later
"""

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail")

    class Meta:
        model = User
        fields = ('url', 'id', 'username',)
        # extra_kwargs = {'url': {'view_name': 'api:user-detail'}}
        # fields = ('id', 'username',)


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    messages = serializers.StringRelatedField(many=True, read_only=True)    

    class Meta:
        model = Channel
        fields = ('users', 'subject', 'messages')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Message
        fields = ('owner', 'channel', 'date', 'text')