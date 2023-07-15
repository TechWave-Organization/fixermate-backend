import uuid 
from django.db import models
from src.person.models import Person
from src.user.manager import UserManager

#Create your models here
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField(max_length=100)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"