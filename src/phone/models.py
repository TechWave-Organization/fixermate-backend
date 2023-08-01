import uuid
from django.db import models
from src.person.models import Person
from src.phone.manager import PhoneManager
from src.base.models import BaseModel


class Phone(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    number_phone = models.PositiveIntegerField
    objects = PhoneManager()
    
    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"

