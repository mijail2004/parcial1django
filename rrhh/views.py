from rest_framework import viewsets
from .models import Empleado, Proyecto, Asignacion
from .serializers import EmpleadoSerializer, ProyectoSerializer, AsignacionSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all().order_by("id")
    serializer_class = EmpleadoSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all().order_by("id")
    serializer_class = ProyectoSerializer

class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.select_related("empleado", "proyecto").all().order_by("-id")
    serializer_class = AsignacionSerializer

