from project.api.views import UserViewSet
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Grailed API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url('^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration', include('rest_auth.registration.urls')),
]
