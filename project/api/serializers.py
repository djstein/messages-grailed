from django.contrib.auth.models import User
from rest_framework import serializers
"""
Very similar to Django Form class
Use ModelSerializers later
"""

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username',)
