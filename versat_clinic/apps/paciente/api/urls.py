from rest_framework.routers import DefaultRouter

from versat_clinic.apps.paciente.api.paciente_viewset import PacienteViewSet

router = DefaultRouter()

router.register(r'', PacienteViewSet, basename='paciente')

urlpatterns = router.urls
