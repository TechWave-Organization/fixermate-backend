from django.db import models
from src.base.models import BaseModel
from src.client.manager import ClientManager
from src.person.models import Person
import uuid
# Create your models here.

class Client(BaseModel):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    objects = ClientManager()

    class Meta:
        verbose_name= 'Client'
        verbose_name_plural= 'Clients'