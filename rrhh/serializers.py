from rest_framework import serializers
from .models import Empleado, Proyecto, Asignacion

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = [
            "id", "nombre", "descripcion", "fecha_inicio", "fecha_fin", "completado"
        ]

class EmpleadoSerializer(serializers.ModelSerializer):
    proyecto = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Empleado
        fields = [
            "id", "nombre", "apellido", "email", "telefono",
            "direccion", "pais", "puesto", "salario",
            "fecha_contratacion", "activo", "proyecto"
        ]

    def get_proyecto(self, obj):
        if hasattr(obj, "asignacion") and obj.asignacion:
            return obj.asignacion.proyecto.nombre
        return None

class AsignacionSerializer(serializers.ModelSerializer):
    empleado_nombre = serializers.CharField(source="empleado.__str__", read_only=True)
    proyecto_nombre = serializers.CharField(source="proyecto.nombre", read_only=True)

    class Meta:
        model = Asignacion
        fields = ["id", "empleado", "proyecto", "empleado_nombre", "proyecto_nombre", "fecha_asignacion"]

    def validate(self, attrs):
        empleado = attrs.get("empleado")
        if empleado and hasattr(empleado, "asignacion"):
            raise serializers.ValidationError("Este empleado ya está asignado a un proyecto.")
        return attrs
