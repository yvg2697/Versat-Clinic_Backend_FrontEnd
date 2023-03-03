from rest_framework.routers import DefaultRouter

from versat_clinic.apps.trabajador.api.trabajador_viewset import TrabajadorViewSet

router = DefaultRouter()

router.register(r'', TrabajadorViewSet, basename='trabajador')

urlpatterns = router.urls
