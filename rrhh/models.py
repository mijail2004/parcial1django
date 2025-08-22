from django.db import models
from django.core.exceptions import ValidationError

class Proyecto(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    completado = models.BooleanField(default=False)

    def clean(self):
        if self.fecha_fin < self.fecha_inicio:
            raise ValidationError("fecha_fin no puede ser anterior a fecha_inicio.")

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=30, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    pais = models.CharField(max_length=80, blank=True)
    puesto = models.CharField(max_length=120, blank=True)
    salario = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha_contratacion = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

#aquí se define que un empleado puede trabajar en un solo proyecto a la vez :v
class Asignacion(models.Model):

    empleado = models.OneToOneField(
        Empleado, on_delete=models.CASCADE, related_name="asignacion"
    )
    proyecto = models.ForeignKey(
        Proyecto, on_delete=models.CASCADE, related_name="asignaciones"
    )
    fecha_asignacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.empleado} → {self.proyecto}"
