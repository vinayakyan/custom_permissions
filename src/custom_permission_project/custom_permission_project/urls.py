from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post_app.views import PostViewSet
from rest_framework_simplejwt.views import token_refresh, token_obtain_pair

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('auth_app.urls')),
    path('access/', token_obtain_pair, name='access-token'),
    path('refresh/', token_refresh, name='refresh-token'),

]
