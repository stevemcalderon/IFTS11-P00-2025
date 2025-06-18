from django.db import models

class Perro(models.Model):
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
        ('adoptado', 'Adoptado'),
    ]

    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    tamaño = models.CharField(max_length=30)
    peso = models.FloatField(null=True, blank=True)
    estado_salud = models.TextField()
    vacunado = models.BooleanField
    estado = models.CharField(max_length=20, choices=ESTADOS, default='disponible')
    temperamento = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.raza}) - {self.estado}"


class UsuarioAdoptante(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    preferencia_raza = models.CharField(max_length=50, blank=True, null=True)
    preferencia_edad = models.IntegerField(blank=True, null=True)
    preferencia_tamaño = models.CharField(max_length=30, blank=True, null=True)
    historial_adopciones = models.ManyToManyField(Perro, blank=True)
    peso = models.FloatField(null=True, blank=True)
    


    def __str__(self):
        return self.nombre
    
from django.utils import timezone

class PostulacionAdopcion(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    fecha_postulacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} postuló por {self.perro.nombre}"

