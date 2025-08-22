from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet, ProyectoViewSet, AsignacionViewSet

router = DefaultRouter()
router.register(r"empleados", EmpleadoViewSet, basename="empleados")
router.register(r"proyectos", ProyectoViewSet, basename="proyectos")
router.register(r"asignar", AsignacionViewSet, basename="asignar") 

urlpatterns = [
    path("", include(router.urls)),
]
