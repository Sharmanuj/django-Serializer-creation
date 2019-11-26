from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from api import views
from rest_framework_swagger.views import get_swagger_view
from django.contrib import admin
from django.urls import path, include

schema_view = get_swagger_view(title='Pastebin API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'topics', views.TopicViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token, name='api-token-auth'),
    path('docs/', get_swagger_view(title='API Docs'), name='api_docs'),
    path('', schema_view),
]
