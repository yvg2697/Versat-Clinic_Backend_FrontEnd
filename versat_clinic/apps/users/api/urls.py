from rest_framework.routers import DefaultRouter

from versat_clinic.apps.users.api.user_viewset import UserViewSet

router = DefaultRouter()

router.register(r'', UserViewSet, basename='users')

urlpatterns = router.urls
