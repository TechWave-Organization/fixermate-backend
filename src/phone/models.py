import uuid
from django.db import models
from src.person.models import Person
from src.phone.manager import PhoneManager




class Phone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    number_phone = models.IntegerField
    objects = PhoneManager()
    
    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"

