from django.contrib.auth.models import User
from project.api.models import Channel, Message
from project.api.permissions import IsOwnerOrReadOnly
from project.api.serializers import  ChannelSerializer, MessageSerializer, UserSerializer
from rest_framework import permissions, viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'messages': reverse('messages-list', request=request, format=format),
    })


class CreateListRetrieveViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class MessageViewSet(CreateListRetrieveViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update', and 'destory actions'

    Additionally we also provide an  'reply' action
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_class = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
