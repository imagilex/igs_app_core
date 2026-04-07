from django.db import models


class ExampleItem(models.Model):
    nombre = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
