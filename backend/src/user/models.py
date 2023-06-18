import uuid 
from django.db import models

from src.person.models import Person

#Create your models here
class user(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField(max_length=100)
    person_id = models.ForeignKey(Person.id, on_delete=models.CASCADE, null=True)
