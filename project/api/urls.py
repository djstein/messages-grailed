from project.api.views import ChannelViewSet, MessageViewSet, UserViewSet
from django.conf.urls import url, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.authtoken import views


schema_view = get_schema_view(title='Grailed API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'channels', ChannelViewSet)
router.register(r'messages', MessageViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^', include('rest_auth.urls')),
    url(r'^registration/$', include('rest_auth.registration.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token), # fet token with username and password
]