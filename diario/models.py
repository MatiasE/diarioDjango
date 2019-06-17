from django.db import models
from django.utils import timezone

# Create your models here.
class Articulo(models.Model):
    autor = models.CharField(max_length = 50)
    titulo = models.CharField(max_length = 100)
    texto = models.TextField()
    dia_creada = models.DateTimeField(default = timezone.now)
    dia_publicada = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo