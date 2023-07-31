import uuid
from django.db import models
from src.person.models import Person
from src.user.manager import UserManager
from src.base.models import BaseModel



class User(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
