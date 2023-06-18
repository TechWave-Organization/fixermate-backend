import uuid
from django.db import models

# Create your models here.
class Person(models.Model):
    id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    departament = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
