from django.db import models
from datetime import datetime
from django.urls import reverse


class Empresa(models.Model):
    nombre = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse('solicitud:empresa-update', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        pass


class Ciudad(models.Model):
    nombre = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse('solicitud:ciudad-update', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = 'Ciudades'


class Registro(models.Model):
    tiempo_atencion = models.DateTimeField(
        max_length=128, default=datetime.now,
        verbose_name='Fecha y hora de atención')
    tiempo_fin_atencion = models.DateTimeField(
        max_length=128, default=datetime.now,
        verbose_name='Fecha y hora final de atención')
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    asunto = models.CharField(max_length=128)
    respuesta = models.TextField()
    fecha_solicitud = models.DateField(default=datetime.today)

    def get_absolute_url(self):
        return reverse('solicitud:registro-update', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.asunto}"

    class Meta:
        pass
